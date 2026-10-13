# Cloud tools, access, job state and delivery

## Execution boundary

Production uses the GPT-Social-Media cloud host and connected cloud services. No local Mac, desktop Adobe installation or local heartbeat is a production dependency. Use the actual host's supported tools; do not copy tool names or authentication assumptions from a different chat.

For a required operation, prefer a suitable available connector/API. Use another verified cloud service for an operation not covered by that interface. A provider's marketing page, exposed tool or successful catalogue read does not prove upload, render, playback, editable export or access in this environment.

Use existing authorisation, but inspect current operation inputs, quote configured cost and respect the agreed ceiling. Do not repeatedly regenerate a failed shot without a concrete correction. Preserve accepted references. Tools that already handle an operation should be used through their documented workflows; obey their upload, status and polling requirements.

## Adobe and other providers

Adobe operations may include image editing, font discovery, speech enhancement, video metadata, frame rendering, resize and clip/audio timeline rendering. The observed timeline schema had timing, basic visual transforms and audio gain; it did not establish full desktop Premiere/After Effects/Audition control or temporal video segmentation. Discover the current schema before choosing it.

Before Adobe use, call its mandatory initialiser once when provided by the host and read its routing rules. Pass valid cloud asset identities or accepted URLs; an inaccessible host filesystem path is not a cloud asset. Use documented upload/import routes and inspect actual success. Do not manufacture asset IDs or derive them from account URLs.

OpenArt and Higgsfield: discover available models/modes, exact configuration/schema and costs before submitting. Image-to-video and subject-reference generation have different semantics. Retain selected reference identities, source prompts/settings, job IDs and usable output files. Provider credits are separate units, not a shared budget.

ImagineArt: verify the authenticated organisation, required tool and Film Studio access. Website features and connector operations can differ.

OpenAI image tools: use for requested generation/editing of artwork and backdrop images where available. They do not establish whole-video background replacement.

Do not require Suno execution access: the creator receives the prompt package, generates the song and returns the selected audio.

## Verify in this environment

For each needed service record:
- current host, verification date, operation and authenticated scope (without secrets);
- exposed, catalogue_read_verified, operation_verified or unavailable;
- input transfer, output export/storage and visual/playback verification separately;
- diagnostic information useful for correcting a failure without raw credentials or signed links.

Perform the smallest relevant end-to-end test with a suitable authorised non-private test asset: upload/import, metadata, a short requested operation, export to durable storage and inspection. Do not claim a media test from a catalogue result. Generation that charges credits needs the actual authorised budget.

### Prior observations - historical, not environment certification

On 13 October 2026, in the skill-authoring chat, Adobe initialisation, a 115-preset catalogue, Fonts search and authenticated Creative Cloud search responded. Cloud Markdown-to-PDF creation, document properties, extraction and PNG ZIP conversion succeeded. Individual-page PNG listing was rejected for external storage; ZIP output succeeded. No video render, speech-enhancement or moving-subject background replacement was validated.

Those observations do not certify GPT-Social-Media environment access. Discover and test its connections again. Do not copy private Adobe directory identities into this public repository.

## Storage and public-repository boundary

This repository is public. Keep only reusable instructions, templates, validation and non-private examples in Git. Original poems, voices, photos, recordings, generated assets, private manifests, provider responses containing identifiers, credentials and signed URLs belong in durable private cloud storage.

Use secure host/service configuration for credentials; never put them in prompts, public files, build logs or commits. Do not turn failed access into public asset sharing. Persist stable private asset IDs/keys and access-controlled retrieval; expiring URLs alone are not durable delivery.

A provider sandbox or temporary CI artifact is not the master archive. Export finished media before any ephemeral worker disappears.

## Job and completion state

Instantiate [job-manifest.json](../assets/templates/job-manifest.json) privately. Record source/audio versions, selected in/out passage, costs, job IDs, output asset keys and QA.

Use states: input_received, suno_package_ready, awaiting_song, producing, reviewing, ready_for_user_review, revision_requested, approved, published, failed, needs_input.

Checkpoint before waiting for external work. A queued task is not done; poll through supported provider status tools or a configured cloud continuation. Do not promise a job will keep running after the host stops unless that mechanism actually exists.

At ready_for_user_review:
- both requested video versions or both requested artwork layouts are accessible;
- full render/audio and typography checks have passed;
- deliverables include captions, covers, MUSIC.md and UPLOAD-PACKAGE.md where applicable;
- editable sources or honest rebuild materials accompany the result;
- any material unverified limitation is identified.

Return **Ready for your review** and preview/link every requested output in the originating chat. Use the host's configured completion alert, with a real job/turn-completion event where supported. Do not claim push/email delivery from a written instruction alone. Notify only for readiness, failure or required input; no repeated unchanged-status messages.

The user reviews before publication. Publishing requires their approval within an authorised publishing workflow and an actual post/platform record before it is reported as published.

## Current product references

Refresh drifting instructions when needed:
- [OpenAI cloud environments](https://learn.chatgpt.com/docs/environments/cloud-environments)
- [OpenAI notifications](https://learn.chatgpt.com/docs/notifications)
- [OpenAI skill authoring](https://learn.chatgpt.com/docs/build-skills)
- [Instagram creator Best Practices](https://about.fb.com/news/2024/10/best-practices-education-hub-creators-instagram/)

Use relevant account Insights when available. Label metric denominators, formats and observation ages; separate raw views from engaged viewing and replay-influenced measures. Creative hypotheses do not guarantee virality.
