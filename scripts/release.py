#!/usr/bin/env python3
"""Build only explicitly reviewed, reusable Career Vault files. No network access."""
from pathlib import Path
import hashlib
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
VERSION = '0.1.0'
SKILL_FILES = [
    'SKILL.md', 'references/interview.md', 'references/outputs.md',
    'assets/career-record.md', 'assets/output-templates.md',
]
SOURCE_FILES = [
    'README.md', 'LICENSE', 'CONTRIBUTING.md', '.gitignore',
    'docs/design.md', 'docs/chatgpt.md', 'docs/claude.md', 'docs/privacy.md',
    'docs/pilot.md', 'docs/release.md',
    'docs/superpowers/plans/2026-10-29-career-vault.md',
    'examples/synthetic-journey.md', 'tests/scenarios.md', 'tests/results.md',
    'tests/behavior-transcripts.md', 'tests/review.md', 'scripts/release.py',
] + ['skill/career-vault/' + p for p in SKILL_FILES]

def validate_sources():
    for name in SOURCE_FILES:
        path = ROOT / name
        if not path.is_file() or path.is_symlink():
            raise ValueError(f'Missing file or symlink refused: {name}')
        if path.suffix == '.md':
            content = path.read_text()
            for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', content):
                if '://' in target or target.startswith('#'):
                    continue
                destination = (path.parent / target.split('#')[0]).resolve()
                if not destination.is_relative_to(ROOT) or not destination.is_file():
                    raise ValueError(f'Invalid relative link: {name} -> {target}')
    core = (ROOT/'skill/career-vault/SKILL.md').read_text()
    assert core.startswith('---\nname: career-vault\ndescription: Use when ')
    assert core.split('---', 2)[2].strip(), 'Empty playbook'
    return core

def write_zip(path, pairs):
    with zipfile.ZipFile(path, 'w', zipfile.ZIP_DEFLATED) as archive:
        for name, content in pairs:
            # Fixed timestamp and permission bits make unchanged inputs reproducible.
            info = zipfile.ZipInfo(name, (2026, 10, 29, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, content)
    with zipfile.ZipFile(path) as archive:
        assert archive.testzip() is None
        assert archive.namelist() == [name for name, _ in pairs]

def main():
    validate_sources()
    dist = ROOT/'dist'
    dist.mkdir(exist_ok=True)
    pairs = [('career-vault/'+p, (ROOT/'skill/career-vault'/p).read_bytes()) for p in SKILL_FILES]
    pairs.append(('career-vault/LICENSE', (ROOT/'LICENSE').read_bytes()))
    skill_zip = dist/f'career-vault-skill-{VERSION}.zip'
    write_zip(skill_zip, pairs)
    bundle = dist/'career-vault-playbook.txt'
    sections = [
        f'Career Vault {VERSION} — complete portable playbook\nPrivate pilot. No personal career data is included.\n',
        'For the assistant: Follow the core instructions below. Referenced files are included as named sections in this text. Templates are structures, not user facts. For the user: send the README starter message after providing this file.\n',
    ]
    for name in SKILL_FILES:
        sections.extend([f'\n===== {name} =====\n', (ROOT/'skill/career-vault'/name).read_text()])
    sections.extend(['\n===== LICENSE =====\n', (ROOT/'LICENSE').read_text()])
    bundle.write_text('\n'.join(sections))
    pilot_zip = dist/f'career-vault-pilot-{VERSION}.zip'
    source_pairs = [('career-vault/'+p, (ROOT/p).read_bytes()) for p in SOURCE_FILES]
    source_pairs.extend([
        ('career-vault/dist/'+skill_zip.name, skill_zip.read_bytes()),
        ('career-vault/dist/'+bundle.name, bundle.read_bytes()),
    ])
    write_zip(pilot_zip, source_pairs)
    artifacts = [skill_zip, bundle, pilot_zip]
    (dist/'SHA256SUMS').write_text(''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.name+'\n' for p in artifacts))
    print(f'PASS: {len(SOURCE_FILES)} allowlisted sources, relative file links, skill header, two exact ZIP manifests/CRC checks, complete text bundle and SHA256SUMS')
    for path in artifacts:
        print(f'{path.name}: {path.stat().st_size} bytes')

if __name__ == '__main__':
    main()
