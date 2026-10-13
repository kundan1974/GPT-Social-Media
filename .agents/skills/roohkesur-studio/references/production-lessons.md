# Reusable recitation production lessons

Read these lessons when editing a creator recording, revising its soundtrack or finalizing an approved package. Keep project-specific timings, poems, media, approval messages and asset keys in the private workspace.

## Preserve the performance and source

Keep the untouched upload, exact Unicode poem and original voice track. Inspect rotation metadata, frame rate, audio timing and colour transfer before editing. A phone recording may need orientation correction and HDR-to-SDR conversion; an SDR source must not automatically receive an HDR recipe. Shape Devanagari with a supported font and inspect the rendered text. Speech recognition is a draft aid; unreliable recognition must not overwrite the supplied poem. Label literary stanza overlays separately from word-aligned speech captions.

For files above the attachment-transfer limit, use the creator's private storage upload rather than repeatedly retrying the same attachment. Respect an existing project location. For new projects follow AGENTS.md's workspace convention and the private workspace index.

## Verify sync through content

Trim picture and sound to the same source interval in the filter graph, reset both timestamps and apply corresponding holds or delays. Establish a constant frame rate before frame-duration padding. Do not assume an input seek, matching container durations or zero start times proves lip sync.

Compare the edited voice waveform and matching face frames against the synchronized source at several speaking points across the excerpt, and check opening and ending holds. Use an explicit frame rate when extracting verification frames. Save measurements and full-decode results privately. Adapt checkpoints and crop geometry to the current duration and layout; previous production scripts may contain preset assumptions.

## Mix music without moving the voice

When the picture is accepted, copy its encoded video stream while mixing authorised music. Preserve voice timing; account for any limiter latency. Verify video packet hashes and presentation/decode timestamps, then compare voice timing at several speaking points.

Start with a restrained music level, use gentle fades and voice-driven ducking, and assess softer phrases as well as louder ones. Loudness and ducking settings are starting points, not universal presets. Background music filling pauses can reduce whole-window waveform correlation without introducing a delay; measure timing separately and assess voice/background balance during active speech. Do not silently loop or stretch a short music source. Retain the accepted voice-only version and document the supplied track's provenance without certifying unverified licence rights.

## Finalize the reviewed revision

Record creator approval against the exact reviewed revision and output hashes. Preserve superseded versions, promote accepted exports without rerendering, and update companion documents and the private job manifest consistently. Include both versions, covers, caption.txt, MUSIC.md, UPLOAD-PACKAGE.md, editable text/timings, rebuild instructions and QA evidence.

Verify private ACLs and complete downloaded SHA-256 equality. Check archive integrity. Keep an archive's own hash in a separate index to avoid self-referential manifests. Keep stable private storage keys; signed download URLs expire and are access credentials. Publish only through an authenticated supported workflow and record actual platform post IDs/URLs before calling the work published. Creator approval and a completed archive do not themselves prove social submission. If approval is already given for the reviewed revision, preserve it while resolving a missing connection rather than requesting approval again.

## Connections, notifications and memory

Recheck needed provider operations on the current host. Catalogue access does not prove import, rendering, export or publishing. Quote actual generation costs before paid work; provider credits are not permission to spend. A verified cloud-host render can be a valid production route when a provider operation is unavailable.

Completion monitors must use a supported chat-read/status tool, stay quiet while unchanged, notify once for meaningful changes and disable after success or an unrecoverable access failure. Do not claim notification delivery without a real event. Report automated checks and creator review separately; sampled checks do not establish exhaustive human playback review.

Maintain reusable decisions here and in AGENTS.md; maintain project-specific history in private storage. Future tasks using this repository should load these instructions. Do not claim a separate global memory or authenticated connection was configured merely because instructions were saved.
