Friends Manual Scene Segmentation: Guidelines
==============================
Authors: Maryse Lapierre, Marie St-Laurent
<br>
<br>

**1. OVERARCHING GOAL**

This manual segmentation technique was developed to enrich the *friends* dataset of the Courtois Project on Neuronal Modelling ((CNeuroMod)[http://docs.cneuromod.ca/])<sup>1</sup>  which consists of ~60h of fMRI data per subject (n=6) acquired while they watched seasons 1 to 6 of the sitcom Friends. To accompany these fMRI data, we are compiling a set of annotations that characterize low and high-level dimensions in the set of video stimuli.

For manual scene segmentation, Friends episodes were segmented into meaningful, cohesive units of story by human raters. Scene boundaries were flagged whenever a rater noticed a location change, time jump, character departure or entry, goal change or another transitions (e.g., musical interlude, theme song). The following segmentation rules and guidelines were initially put together by Laurie Charest, Jeni Chen and Marie St-Laurent, and formalized, expanded and clarified by Maryse Lapierre and Marie St-Laurent.

1. Boyle JA , Pinsard B , Boukhdhir A , Belleville S, Brambatti S, Chen J, Cohen-Adad J, Cyr A, Fuente, Rainville P, Bellec P. The Courtois project on neuronal modelling – first data release. In: 2020.
<br>

**2. SCENES AND SEGMENTS**

**Scenes** are sequences of movie frames that feature events contiguous in time and space. A scene corresponds to a portion of an episode’s story that is bound by time jumps, location changes and other transition markers (e.g., musical interludes, fade outs, theme song).

Typically, a **scene** contains multiple **segments**. **Segments** are cohesive story elements that are nested within scenes. The same scene can include more than one story segment during which different characters address different issues (e.g., an extended scene of the characters hanging out at Monica's apartment can include different segments during which Monica frets over her parents visiting, Rachel looks for her lost engagement ring, and then Ross announces to his friends that his ex wife is pregnant). For example, episode s1e06a features a long scene (beginning around 07:25) that contains a series of segments that correspond to flashbacks interweaved with the present.

The first **scene** is numbered 001, the second scene 002, and so on until the end of a half-episode (for CNeuroMod, full Friends episodes were split into two halves, typically a & b, that were shown as separate fMRI runs of ~12 minutes each). Segments are also numbered from 001, 002 and so on until the end of the half episode. 

Boundaries between **segments** are flagged by the rater based on perceived transitions in the storyline. Boundaries are noted whenever the rater notices one or several of the following changes: a location change, a time jump, a character departure or entry, a goal change or a transition that reflects cinematographic editing (e.g., musical inter-scene transitions, theme song).  

The average **segment** length varies from ~45 seconds to a few minutes (between 3-4 minutes). There are exceptions, as some segments can last more than 4 minutes. Segments are very rarely shorter than 30 seconds. The last segment of a half-episode starts when the screen fades to black and lasts until the end of the .mkv
<br>
<br>

**3. BOUNDARY ANNOTATIONS PER TYPES**

Boundaries indicate transitions between scenes and/or segments.

**3.1 Musical transition**

Friends episodes include a few transitions between scenes that feature outdoor footage of New York city (e.g., views from outside the friends’ apartment building) accompanied by music. Those few seconds of transition (~3-4 second) are segmented separately一they are their own **scenes**一from other scenes that feature the main cast. These moments of musical transition emphasize the switch between two scenes.

**3.2 Character entry**

When annotating the entry of a character into a scene or segment, boundaries are marked only if a character is involved in the ongoing scene (if their presence contributes to the story). If a background character passes behind the main scene, this is not considered a boundary一it is not annotated.

If a character arrives within a window of 5 seconds from the **onset of the scene or segment**, it is not considered a boundary (no annotation required)一it is not a scene change, it is parts of the scene being set.

When there is a time lapse between the scene onset and the character entry (>5 seconds), a boundary is marked to annotate the onset of a new segment that begins with a character entry一but only if the character’s arrival changes the main goal (focus) of the ongoing scene.


**3.3 Character leaving**

A character exit is characterized by the departure of a character from the main scene. Typically, a character departure is accompanied by a change in the ongoing scene’s focus / goal. If a character disappears from the screen for a moment but is still “around” (e.g., the camera changes focus, the character briefly goes behind the scene), it is not annotated as a character-leaving boundary.

**3.4 Time jump**

A time jump is annotated as a boundary when there is a sharp time progression (in the past or in the future, as during a flashback) between two segments or scenes.  

**3.5 Goal change**

A goal change reflects a change of focus in the ongoing story. It could be a change in the topic of conversation, a switch in the characters’ current goals, etc. Goal changes orient a series of actions or reactions in the characters.

Note that a "goal change" boundary should not be annotated if an occurrence with the potential to change the focus/goal of an ongoing scene occurs at the very end of a segment. In this scenario, the scene ends too quickly after the event for it to cause a series of actions or reactions that re-orient the story arc within an ongoing scene: the re-orienting event does not mark the onset of a new segment. E.g., In s1e03a at 02:48, Phoebe quietly opens a soda and finds a thumb inside. The scene cuts 2 seconds later, so finding the thumb is not a “goal change” boundary between two story segments because it lacks sufficient time to re-orient the scene.

Goal changes can be subtle and are more subjective to the rater than other types of scene boundaries. For this reason, our policy is that goal changes should only be annotated if they are obvious to the rater.

**3.6 Location change**

A location change boundary is marked when the location changes between two scene segments (e.g., characters move from one apartment to another), or when consecutive scenes take place in different locations. E.g., location change boundaries are marked between consecutive scenes set in Monica’s apartment and the coffee shop, respectively.

**3.7 Theme song**

A theme song boundary is marked at the onset of the segment that corresponds to the opening theme song.

**3.8 End**

An “end” boundary is marked as the scene fades at the end of a half-episode. It marks the onset of the episode’s last segment, which starts with the fading-out and lasts until the end of the video (last .mkv frame).
<br>
<br>

**4. LOCATION ANNOTATIONS**

The location annotations indicate where a scene or segment takes place among the following options:
- **Apartment 1** corresponds to the purple apartment originally shared by Monica and Rachel.
- **Apartment 2** corresponds to Chandler and Joey’s beige apartment, across from Apartment 1.
- **Apartment 3** corresponds to Ross’ apartment.
- **Apartment 4** is Phoebe's apartment.
- **Coffee Shop** corresponds to Central Perk, the local coffee place where the characters hang out.
- **Outside** indicates any scene or segment filmed outdoors (e.g. New York view, street view, etc.).
- **Other** corresponds to all the other locations that are indoor (e.g., character work places, bank, theater, etc.).
<br>

**5. SEGMENT CAPTIONS**

Captions are complete sentences that provide the gist of each segment (what is happening in the story's plot). Captions were originally written by the main rater in her native French, and then translated into English using the online tool deepl (https://www.deepl.com/translator), with some manual editing to resolve ambiguities.
<br>
<br>

**6. SPECIAL CLAUSES AND EXCEPTIONS**

**6.1 Flashbacks**

When it comes to flashbacks, the first question to ask is: Did the location change between scenes?

If the time is not continuous, a time jump is marked. If the location is also different, a time jump and a location change both mark the onset of a new segment. If a character enters a scene during the flashback, we also consider it a boundary (character entry). The first example of flashback is s1e05a at 07:01 to 08:41: the characters are in the same coffee shop in the present time and the flashback, so no location change is noted between the segments - just time jumps. If different characters are featured in the present and in the flashback, no character entry / leaving is noted (unless someone arrives or departs within the ongoing scene), just the time jump.

**6.2 Known outdoors locations**

1. The balcony at Monica and Rachel's apartment is considered the same place as their apartment even though it is outdoors. So there is no location change between the balcony and the main apartment (although goal changes can indicate boundaries between indoor and outdoor segments). Outdoor balcony segments receive both the “apartment 1” and the “outdoors” location labels.

2. The terrace in front of the coffee shop is considered the same place as the coffee shop (indoors) even if it is outside;  there is no location change. Patio and indoor coffee shop segments receive both the “coffee shop” and the “outdoors” location labels.

**6.3 Phone calls**

When the phone rings, we annotate a character entry (the caller) and a goal change (the scene’s focus switches to the phone conversation).

IF the caller is shown on screen speaking from a different location, we also annotate a location change一as a new location is "added" to the scene that reflects where the caller is based. In that case, the segment’s location annotation should reflect the 2 locations connected by the call (e.g., “apartment 1” and “other”). The entire phone call is then considered a single segment, even if the on-screen character location alternates between the two callers. That is, no location change is noted when the viewpoint switches from one caller to the other throughout the call. Then, if the scene continues after the call ends, we annotate a “character leaving” boundary, and the new segment’s location annotation should only reflect where the remainder of the scene is played.

**6.4. Video tape**

When a scene includes characters watching a video (e.g., if the friends start watching an old video of themselves), the boundary is considered a goal change only. No location change, time jump or character entry is noted because it is a recorded scene and not an active one: the scene involves the characters watching themselves, it is not a flashback. Example: When the characters watch Monica and Rachel’s prom video in s2e14b at 05:06.
