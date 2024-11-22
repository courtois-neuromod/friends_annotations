Friends Manual Scene Segmentation: Guidelines
==============================
Authors: Maryse Lapierre, Marie St-Laurent


**1. OVERARCHING GOAL**

This manual segmentation technique was developed to enrich the friends dataset of the Courtois Project on Neuronal Modelling (CNeuroMod)<sup>1</sup>  which consists of ~60h of fMRI data per subject (n=6) acquired while they watched seasons 1 to 6 of the sitcom Friends. To accompany these fMRI data, we are compiling a set of annotations that characterize low and high-level dimensions in the set of video stimuli.

For manual scene segmentation, Friends episodes were segmented into meaningful, cohesive units of story. Scene boundaries were flagged whenever a rater noticed a location change, time jump, character departure or entry, goal change or another transitions (e.g., musical interlude, theme song). The following segmentation rules and guidelines were initially put together by Laurie Charest, Jeni Chen and Marie St-Laurent, and formalized, expanded and clarified by Maryse Lapierre and Marie St-Laurent.

1. Boyle JA , Pinsard B , Boukhdhir A , Belleville S, Brambatti S, Chen J, Cohen-Adad J, Cyr A, Fuente, Rainville P, Bellec P. The Courtois project on neuronal modelling – first data release. In: 2020.

**2. SCENES AND SEGMENTS**

Scenes are sequences of movie frames that feature events contiguous in time and space. A scene corresponds to a portion of an episode’s story that is bound by time jumps, location changes and other transition markers (e.g., musical interludes, fade outs, theme song).

Typically, a scene contains multiple segments. Segments are cohesive story elements that are nested within scenes. The same scene can include more than one story segment during which different characters address different issues (e.g., an extended scene of the characters hanging out at Monica's apartment can include different segments during which Monica frets over her parents visiting, Rachel looks for her lost engagement ring, and then Ross announces to his friends that his ex wife is pregnant). For example, episode s1e06a features a long scene (beginning around 07:25) that contains a series of segments that correspond to flashbacks interweaved with the present.

The first scene is numbered 001, the second 002, and so on until the end of a half-episode (for CNeuroMod, full Friends episodes were split into two halves, typically a & b, that were shown as separate fMRI runs of ~12 minutes each). Segments are also numbered from 001, 002 and so on until the end of the half episode.

Boundaries between segments are flagged by the rater based on perceived transitions in the storyline. Boundaries are noted whenever the rater notices one or several of the following changes: a location change, a time jump, a character departure or entry, a goal change or a transition that reflects cinematographic editing (e.g., musical inter-scene transitions, theme song).  

The average segment length varies from ~45 seconds to a few minutes (between 3-4 minutes). There are exceptions, as some segments can last more than 4 minutes. Segments are very rarely shorter than 30 seconds. The last segment (the one at the end) starts when the screen fades to black at the end of the .mkv

**3. BOUNDARY TYPES**

**3.1 Musical transition**

Friends episodes include a few transitions between scenes that feature outdoor footage of New York city (e.g., views from outside their apartment building) accompanied by music. Those few seconds of transition (~3-4 second) are segmented separately - they are their own scenes - from other scenes that feature the main cast. These moments of musical transition emphasize the change between two scenes.

**3.2 Character entry**

When annotating the entry of a character into a scene or segment, it must be a character who is involved in the scene that is taking place. If a background character is just passing behind the main scene, it is not considered a boundary (we do not annotate it).

If a character enters within a window of less than 5 seconds from the scene or segment onset, we do not consider it a boundary (no annotation required) since the entrance occurs at the very beginning of the scene or segment - it is not a scene change, rather the scene is being established.

When there is a time lapse between the scene onset and the character entry (after 5 seconds), a boundary is annotated to mark the onset of a new segment starting with a character entry - but only if the character’s arrival changes the main goal (focus) of the ongoing scene.

**3.3 Character leaving**

A character exit is characterized by the departure of a character from the main scene. If a character disappears from the screen to go behind the scene (but is still around), we do not annotate it as a boundary (character leaving).

**3.4 Time jump**

A time jump is annotated as a boundary when there is a sharp time progression (in the past or future) between two segments or scenes.  

**3.5 Goal change**

A goal change reflects a change of focus in the story (e.g., a change in the topic of conversation, a switch in the characters’ current goals, etc.). Goal changes orient a series of actions or reactions in the characters.
Note that a "goal change" boundary should not be annotated if an event that changes the focus/goal of the scene occurs as a segment ends - in that scenario, the event does not cause a series of actions or reactions that re-orient the story arc within an ongoing scene (it does not mark the onset of a new segment). Also, if an event occurs at the very end of a segment while the story cuts to another segment, no boundary should be annotated. E.g., Phoebe quietly opens her soda and finds a thumb inside s1e03a at 02:48. The scene cuts 2 seconds later, so finding the thumb is not a “goal change” boundary between two story segments.

Because goal changes can be subtle and are more subjective than other types of scene boundaries, goal changes are only annotated if they are obvious to the rater.

**3.6 Location change**

A location change boundary is annotated when the location changes between two scene segments, or when consecutive scenes take place in different locations. E.g., consecutive scenesset in Monica’s apartment and the coffee shop, respectively.

**3.7 Theme song**

Segments correspond to the opening theme song.

**3.8 End**

“End” boundaries correspond to the end of a half-episode.


**4. LOCATION**

Annotations specify where a scene or segment took place among the following options:
Apartment 1 corresponds to the purple apartment originally shared by Monica and Rachel.
Apartment 2 corresponds to Chandler and Joey’s beige apartment, across from Apartment 1.
Apartment 3 corresponds to Ross’ apartment.
Apartment 4 is Phoebe's apartment.
Coffee Shop corresponds to Central Perk, the local coffee place where the characters hang out.
Outside indicates any scene or segment filmed outdoors (e.g. New York view, street view, etc.).
Other corresponds to all the other locations that are indoor (e.g., character work places, bank, theater, etc.).


**5. CAPTIONS**

Captions are complete sentences that provide the gist of each segment (what is happening in the plot). Captions were originally written by the main rater in her native French, and then translated into English using the online tool deepl (https://www.deepl.com/translator), with some manual editing to resolve ambiguities.


**6. SPECIAL CLAUSES AND EXCEPTIONS**

**6.1 Flashbacks**

When it comes to flashbacks, the first question to ask is: Did the location change between scenes?

If the time is not continuous, a time jump is marked. If the location is also different, a time jump and a location change both mark a new segment. If a character enters during the flashback, we also consider it a boundary. The first example of flashback is s1e05a at 07:01 to 08:41: the characters are in the same coffee shop in the present and the flashback, so no location change is noted between segments - just time jumps.

**6.2 Known outdoors locations**

1. The balcony at Monica and Rachel's apartment is considered the same place as their apartment even though it is outdoors. So there is no location change between the balcony and the main apartment (although goal changes can be boundaries between indoor and outdoor segments). Outdoor balcony segments take both the “appartment 1” and the “outdoors” labels.

2. The terrace in front of the coffee shop is considered the same place as the coffee shop (indoors) even if it is outside;  there is no location change. Patio and indoor coffee shop segments take both the “coffee shop” and the “outdoors” labels.

**6.3 Phone calls**

When the phone rings, we annotate a character entry (the caller), goal change (focus switches to phone conversation), and location change - as a new location is "added" that reflects where the caller is based; we also consider the segment’s location to match the 2 locations connected by the call (e.g., “apartment 1” and “other”). The entire phone call is considered one segment even if the on-screen character location alternates between the two callers : no location change is noted when the viewpoint changes from one caller to the other during the call. Then, if the scene continues after the call has ended, we annotate a “character leaving” boundary, and the new segment’s location only matches where the rest of the scene is played.

**6.4. Video tape**

When a scene includes characters viewing a video, the boundary is considered a goal change only. No location change or character entry is noted because it is a recorded scene and not an active one. Example: Monica and Rachel’s prom video from s2e14b at 05:06.
