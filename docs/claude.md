# Use Career Vault with Claude

Checked against official documentation on October 29, 2026. Account/workspace settings and interfaces can change.

## No-install path

Start a new Claude conversation. Upload the complete `career-vault-playbook.txt` release file where supported, or paste its contents. Send the README starter message and ask Claude to confirm which instructions it could read. Answer the goal question first. Choose typing or voice if available. Keep a private exported career record before stopping.

If attachments or links are inaccessible, paste text. Do not assume an unread portfolio URL has been reviewed. You can use the playbook anywhere Claude can read the content; it does not depend on an installed skill.

## Optional skill package

Claude's [official skills guide](https://support.claude.com/en/articles/12512180-use-skills-in-claude) documents custom skill ZIP uploads and the code execution/file creation prerequisite. If available in your account:

1. Enable the required capability described in that guide; managed workspaces may require administrator settings.
2. Open **Customize → Skills**, choose **+ → Create skill → Upload a skill**.
3. Upload `career-vault-skill-0.1.0.zip`, which contains the `career-vault/` folder with `SKILL.md` and its references/templates. Toggle it on.
4. Ask: “Use Career Vault to help me discover my career value and preserve a full portable record.”

The skill contains no executable code or dependencies. Enabling host capabilities does not authorize publishing or transmitting your record. If installation is unavailable, use the no-install path. A GitHub URL does not automatically install it.

## Voice if you want it

Claude's [official voice guide](https://support.claude.com/en/articles/11101966-use-voice-mode) describes voice on web, desktop and mobile. On web/desktop, look for the sound-wave control in the chat; on mobile, use the voice-mode sound-wave icon. Availability and controls may change. Claude allows switching between voice and text within a conversation. Career Vault cannot activate it for you. Confirm uploaded files are accessible and review any misheard names, dates or metrics before approving claims.

## Return later

Provide the playbook and latest private Markdown record. Ask Claude to confirm the current goal and next question, preserve your mode preference and use existing approvals. Do not depend on implicit memory or an old chat to contain everything. Save/export the full record again after meaningful updates.
