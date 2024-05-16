from Square import *
import numpy as np
class DataSet:
    """Class that represents a DataSet that will be trained on SOM, allows grouping operations on points"""
    def __init__(self, data):
        self.points = data

        self.x_values = data[:,0]
        self.y_values = data[:,1]
        self.z_values = data[:,2]
        self.min_x = min(self.x_values)
        self.min_y = min(self.y_values)
        self.max_x = max(self.x_values)
        self.max_y = max(self.y_values)
    """Groups points into smaller squares"""
    def group_points_into_squares(self, x_jump, y_jump, normal_method):
        x_segments_count = int((self.max_x - self.min_x) / x_jump)
        y_segments_count = int((self.max_y - self.min_y) / y_jump)
        segmented_points = np.zeros((x_segments_count+1, y_segments_count+1), dtype=object)

        x = self.min_x
        y = self.min_y

        x_iterator = x_segments_count
        while(x_iterator >= 0):
            y_iterator = y_segments_count
            while(y_iterator >= 0):
                points = [point for point in self.points if point[0] >= x and point[0] < x + x_jump and point[1] >= y and point[1] < y+y_jump]
                x_pos = x_segments_count - x_iterator
                y_pos = y_segments_count - y_iterator
                sq = Square(np.array(points), x_pos, y_pos)
                sq.calculate_normal(normal_method)
                segmented_points[x_pos,y_pos] = sq

                y += y_jump
                y_iterator = y_iterator -1
            x += x_jump
            y = self.min_y
            x_iterator = x_iterator - 1

        self.squares2d = segmented_points
    
    def group_normal_vectors(self, n):
        normal_vectors_list = []
        labels = []
        x_len = self.squares2d.shape[0]
        y_len = self.squares2d.shape[1]
        for x in range(0, x_len-n):
            for y in range(0, y_len-n):
                normals, label = self.get_normals(x,y,n)
                normal_vectors_list.append(normals)
                labels.append(label)
        self.normals_to_train = normal_vectors_list
        self.labels = labels
    
    def get_normals(self, x,y,n):
        """Get normal vectors from search windows at position x and y"""
        normal_vectors = []
        bad_square = 0
        for i in range(x, x+n):
            for j in range(y, y+n):
                if (self.squares2d[i,j].bad_square):
                    bad_square = 1
                normal_vectors.append(self.squares2d[i,j].normal_vector)
        return np.concatenate(normal_vectors).flatten(), bad_square
    
    def randomize(self, percent, indexes = [[0,0]]):
        self.bad_squares = []
        for i in indexes:
            self.squares2d[i[0],i[1]].randomize_points(percent)
            self.bad_squares.append(self.squares2d[i[0],i[1]])

