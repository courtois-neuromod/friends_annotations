for "all videos in folder":
    run detect-adapt "python3 -m PySceneDetect.scenedetect -c configFile.cfg --input /home/steveb/Desktop/LocalAnnot/Data/friends_s01e01a.mkv detect-adaptive list-scenes COLUMNS":

def write_scene_list(output_csv_file: TextIO,
                     scene_list: Iterable[Tuple[FrameTimecode, FrameTimecode]],
                     include_cut_list: bool = True,
                     cut_list: Optional[Iterable[FrameTimecode]] = None) -> None:

# Writes the given list of scenes to an output file handle in CSV format.
#     Arguments:
#         output_csv_file: Handle to open file in write mode.
#         COLUMNS: tells what columns are needed in CSV File (list of columns)
#         scene_list: List of pairs of FrameTimecodes denoting each scene's start/end FrameTimecode.
#         include_cut_list: Bool indicating if the first row should include the timecodes where
#             each scene starts. Should be set to False if RFC 4180 compliant CSV output is required.
#         cut_list: Optional list of FrameTimecode objects denoting the cut list (i.e. the frames
#             in the video that need to be split to generate individual scenes). If not specified,
#             the cut list is generated using the start times of each scene following the first one.

    csv_writer = csv.writer(output_csv_file, lineterminator='\n')
    # If required, output the cutting list as the first row (i.e. before the header row).
    if include_cut_list:
        csv_writer.writerow(
            ["Timecode List:"] +
            cut_list if cut_list else [start.get_timecode() for start, _ in scene_list[1:]])
    # csv_writer.writerow([
    #     "Scene Number", "Start Frame", "Start Timecode", "Start Time (seconds)", "End Frame",
    #     "End Timecode", "End Time (seconds)", "Length (frames)", "Length (timecode)",
    #     "Length (seconds)"
    # ])
        csv_writer.writerow(COLUMNS)

columnWriter= []

if COLUMNS contains("Scene Number"):
    columnWriter.append('%d' % (i + 1))

if COLUMNS contains("Start Frame"):
    columnWriter.append('%d' % (start.get_frames() + 1))

if COLUMNS contains("Start Timecode"):
    columnWriter.append(start.get_timecode())

if COLUMNS contains("Start Time (seconds)"):
    columnWriter.append('%.3f' % start.get_seconds())

if COLUMNS contains("End Frame"):
    columnWriter.append('%d' % end.get_frames())

if COLUMNS contains("End Timecode"):
    columnWriter.append(end.get_timecode())

if COLUMNS contains("End Time (seconds)"):
    columnWriter.append('%.3f' % end.get_seconds())

if COLUMNS contains("Length (frames)"):
    columnWriter.append('%d' % duration.get_frames())

if COLUMNS contains("Length (timecode)"):
    columnWriter.append(duration.get_timecode())

if COLUMNS contains("Length (seconds)"):
    columnWriter.append('%.3f' % duration.get_seconds())

    for i, (start, end) in enumerate(scene_list):
        duration = end - start
        csv_writer.writerow(columnWriter)
