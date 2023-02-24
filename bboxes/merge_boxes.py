def make_bboxes_same_height(bboxes):
    max_height = max([bbox[3] - bbox[1] for bbox in bboxes])
    for bbox in bboxes:
        height_diff = max_height - (bbox[3] - bbox[1])
        top_diff = height_diff // 2
        bottom_diff = height_diff - top_diff
        bbox[1] -= top_diff
        bbox[3] += bottom_diff
    return bboxes
def merge_vertically_near_boxes_with_labels(bboxes, labels, distance_threshold=15, size_threshold=0.5):
    """
    Merges vertically overlapping boxes that are very near in a single box.

    Args:
        bboxes (list): A list of bounding boxes, where each box is a tuple of
                       (left, top, right, bottom).
        labels (list): A list of labels corresponding to each bounding box.
        distance_threshold (int): The maximum distance between the right side of a box
                                  and the left side of the next box for them to be merged.
        size_threshold (float): The minimum ratio of overlap to the size of the smaller box
                                for two boxes to be considered for merging.

    Returns:
        merged_boxes (list): A list of merged bounding boxes.
        merged_labels (list): A list of labels corresponding to each merged bounding box.
    """
    
    # Sort the boxes by their top coordinate
    sorted_boxes = sorted(zip(make_bboxes_same_height(bboxes), labels), key=lambda box: box[0][1])

    merged_boxes = []
    merged_labels = []
    i = 0

    while i < len(sorted_boxes):
        box, label = sorted_boxes[i]
        j = i + 1
        merged_box = box

        # Check for overlapping boxes
        while j < len(sorted_boxes):
            next_box, next_label = sorted_boxes[j]
            
            # Check if the boxes overlap vertically and are very near
            if (abs(next_box[1] - merged_box[1]) <= 5 and abs(next_box[3] - merged_box[3]) <= 5  and
                    abs(next_box[0] - merged_box[2]) <= distance_threshold):

                # Calculate the overlap ratio
                overlap = min(merged_box[3], next_box[3]) - max(merged_box[1], next_box[1])
                size_ratio = overlap / min(merged_box[3] - merged_box[1], next_box[3] - next_box[1])

                # Merge the boxes if the size ratio is above the threshold
                if size_ratio >= size_threshold:
                    merged_box = (min(merged_box[0], next_box[0]),  # left
                                  min(merged_box[1], next_box[1]),  # top
                                  max(merged_box[2], next_box[2]),  # right
                                  max(merged_box[3], next_box[3]))  # bottom
                    label = label if merged_box[2] - merged_box[0] > next_box[2] - next_box[0] else next_label
                j += 1
            else:
                break

        merged_boxes.append(merged_box)
        merged_labels.append(label)
        i = j

    return merged_boxes, merged_labels
