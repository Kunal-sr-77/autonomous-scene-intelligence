def build_scene(detections):
    """
    Convert raw detections into a simple scene representation.
    """

    objects = set()

    for d in detections:
        objects.add(d["label"])

    scene = {
        "objects": list(objects),
        "num_objects": len(detections),
        "scene_type": "vehicle interaction scene"
    }

    return scene