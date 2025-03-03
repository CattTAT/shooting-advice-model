class dbscan_output:
    def __init__(self, archer_level, archer_eye, grouping_no, g1_size, g1_center, g2_size, g2_center, g3_size, g3_center):
        self.archer_level = archer_level
        self.archer_eye = archer_eye
        self.grouping_no = grouping_no

        self.g1_size = g1_size
        if g1_center is None:
            self.g1_center_coordinate = None
        else:
            self.g1_center_coordinate = [g1_center[0], g1_center[1]]

        self.g2_size = g2_size
        if g2_center is None:
            self.g2_center_coordinate = None
        else:
            self.g2_center_coordinate = [g2_center[0], g2_center[1]]
        
        self.g3_size = g3_size
        if g3_center is None:
            self.g3_center_coordinate = None
        else:
            self.g3_center_coordinate = [g3_center[0], g3_center[1]]

    
