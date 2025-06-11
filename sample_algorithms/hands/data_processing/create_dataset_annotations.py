import os
import json

def merge_coco_annotations(root_folder, output_file):
    merged_data = {"categories": [], "images": [], "annotations": []}
    image_id = 0
    annotation_id = 0
    category_set = set()

    for video_folder in sorted(os.listdir(root_folder)):
        video_path = os.path.join(root_folder, video_folder)
        if not os.path.isdir(video_path):
            continue

        for annotation_file in sorted(os.listdir(video_path)):
            if not annotation_file.endswith(".json"):
                continue

            annotation_path = os.path.join(video_path, annotation_file)
            with open(annotation_path, "r") as f:
                data = json.load(f)

            if not merged_data["categories"]:
                merged_data["categories"] = data["categories"]
                category_set = {cat["id"] for cat in data["categories"]}
            elif {cat["id"] for cat in data["categories"]} != category_set:
                raise ValueError("Category IDs do not match across annotation files.")

            if data["annotations"] is not None:
                for img in data["images"]:
                    new_file_name = f"{video_folder}_{img['file_name'][:6]+img['file_name'][7:]}"
                    img["file_name"] = new_file_name
                    img["id"] = image_id
                    img["height"] = 480
                    img["width"] = 640
                    merged_data["images"].append(img)
                    image_id += 1

                for ann in data["annotations"]:
                    ann["id"] = annotation_id
                    ann["image_id"] = image_id - 1
                    merged_data["annotations"].append(ann)
                    annotation_id += 1

    with open(output_file, "w") as f:
        json.dump(merged_data, f)

    print(f"Merged annotations saved to {output_file}")

split = 'train'
# Input and output folder paths
input_folder = f"coco/{split}"
output_file = f"{split}_annotations.json"

merge_coco_annotations(input_folder, output_file)
