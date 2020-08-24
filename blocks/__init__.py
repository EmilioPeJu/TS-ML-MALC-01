from malcolm.yamlutil import make_block_creator, check_yaml_names

detector_block = make_block_creator(__file__, "detector_block.yaml")
scan_block = make_block_creator(__file__, "scan_block.yaml")
scan_block_no_detector = make_block_creator(__file__, "scan_block_no_detector.yaml")
motion_block = make_block_creator(__file__, "motion_block.yaml")
sim_motor_block = make_block_creator(__file__, "sim_motor_block.yaml")

__all__ = check_yaml_names(globals())


