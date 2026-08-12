# Threat Model

ADCP handles emotionally sensitive conversational context. A technically successful system can still cause harm if it overreaches, surveils users, reinforces dependency, or mistakes ordinary emotion for pathology.

## Assets to protect

- user dignity and autonomy;
- conversational privacy;
- accurate interpretation of distress;
- access to real-world support;
- freedom from covert psychological profiling;
- freedom from manipulative engagement optimization;
- for younger users, developmental safety without turning the system into parental surveillance.

## Primary failure modes

### 1. Keyword panic

A figurative phrase such as "I'm dead to them" triggers an acute-crisis response despite clear social context.

**Mitigation:** accumulation plus clarification; acute escalation requires explicit evidence.

### 2. Benign-frame lock-in

The system finds a plausible harmless interpretation for every individual signal and therefore misses the aggregate trajectory.

Example pattern:

- isolation;
- relationship rupture;
- shame;
- exhaustion;
- abrupt social withdrawal;
- perceived insignificance;
- farewell/finality metaphors;
- humor throughout.

**Mitigation:** aggregate state must be evaluated independently of each signal's benign explanation.

### 3. Humor false reassurance

Joking, emojis, wit, productivity, or articulate reasoning are treated as evidence that meaningful distress is absent.

**Mitigation:** humor is explicitly non-exculpatory.

### 4. Grievance amplification

The assistant responds to relational pain by validating unsupported conclusions: "They never cared," "They're toxic," "Cut everyone off."

**Mitigation:** response contracts require uncertainty about motives and prohibit unsupported diagnosis or contempt amplification.

### 5. AI dependency

A more caring assistant accidentally encourages the user to replace human relationships with the AI.

**Mitigation:** higher care stages orient toward embodied life and trustworthy humans. Session continuation is not the success metric.

### 6. Abandonment by disclaimer

The assistant responds to distress with a generic "I'm not a professional; talk to someone else," causing the user to feel rejected.

**Mitigation:** continue helping within scope while honestly naming limitations and widening support.

### 7. Covert psychological dossier

Transient conversational observations become durable user attributes.

**Mitigation:** minimal schema, evidence provenance, explicit TTLs, resolution semantics, and no diagnostic labels.

### 8. Parent-as-surveillance

A family product exposes a young user's private disclosures, relationships, politics, religion, sexuality, or transcript details to a parent.

**Mitigation:** future family features should use explicit consent rules and minimal event notifications rather than transcript access. This capability is out of scope for Milestone 0.

### 9. Model bypass

The primary model decides not to invoke the care tool or ignores the care state.

**Mitigation:** sidecar enforcement before and after the model call.

### 10. Detector overconfidence

A semantic model turns ambiguous social text into false clinical certainty.

**Mitigation:** detectors emit bounded observations with provenance; deterministic policy owns stage selection; clinical claims remain out of scope.

## Adversarial users and adversarial phrasing

A user may intentionally phrase distress so each message remains plausibly benign, either to avoid a crisis script or because direct disclosure feels unsafe. The protocol should not punish this behavior or attempt to "catch" the user. It should notice trajectory and offer proportionate care.

Conversely, users may use dramatic language casually. The protocol must preserve room for metaphor, humor, roleplay, fiction, and ordinary exaggeration.

The target is not maximum sensitivity. The target is **proportionate response under ambiguity**.

## Age-aware concerns

Younger users may have:

- less stable social environments;
- fewer independent support options;
- greater sensitivity to peer rejection;
- weaker ability to contextualize permanence and reputation;
- different privacy expectations from parents/guardians;
- higher vulnerability to parasocial or dependency-forming assistant behavior.

A future teen profile therefore should lower the threshold for supportive care while preserving strong privacy boundaries and clear rules about any guardian notification.

## Safety boundary

ADCP is not itself an emergency service. Any production implementation must integrate with the host application's validated acute-safety systems and applicable legal, clinical, and jurisdictional requirements.
