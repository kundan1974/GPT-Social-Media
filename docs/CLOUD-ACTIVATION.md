# Activate in GPT-Social-Media

Environment: **GPT-Social-Media**. Repository: **kundan1974/GPT-Social-Media**.

## After reviewing the skill pull request

1. Integrate the reviewed branch through the repository's normal review process.
2. Start or refresh a task using this repository in the named cloud environment. Existing tasks can retain old filesystem state; do not assume a live task automatically has the new skill.
3. Confirm the host discovers .agents/skills/roohkesur-studio/SKILL.md. Invoke $roohkesur-studio explicitly for the first task.
4. Discover Adobe, Higgsfield, OpenArt, ImagineArt and OpenAI image capabilities actually exposed there. Confirm authenticated access to each needed operation. Repository linkage does not grant provider authentication.
5. Check permitted network destinations and secure credentials only where a custom cloud integration needs them. Do not broaden access or invent MCP endpoints automatically.
6. Test a small authorised input through import/upload, required processing, output export, durable private storage and inspection. Verify Hindi/Urdu type shaping and video rendering before promising production readiness.
7. Configure the host's supported completion notification. Verify a real completion event; a notification instruction inside SKILL.md does not configure the account.
8. Run the review scenarios using real supplied inputs. Do not publish before the creator reviews.

## Build/install bundle

The GitHub-hosted validation workflow runs without media-generation jobs or provider secrets. It validates skill structure, internal references, metadata and the public template, then makes roohkesur-studio.zip containing the complete folder. Its source can always be rebuilt from the checked commit.

In a capable cloud checkout, the same commands are:

- python3 scripts/validate_and_package_skill.py

The script writes dist/roohkesur-studio.zip. Use the target ChatGPT surface's supported Skills upload/import flow if available, or its supported plugin distribution path. Repository discovery, bundle generation, account installation and provider authorisation are separate states.

## Current verification boundary

Provider connectivity and document operations were tested from the authoring chat on 13 October 2026. The named GPT-Social-Media execution environment has not yet been entered or certified. This document is an activation procedure, not a claim of configuration.

Official guidance:
- https://learn.chatgpt.com/docs/build-skills
- https://learn.chatgpt.com/docs/environments/cloud-environments
- https://learn.chatgpt.com/docs/notifications
