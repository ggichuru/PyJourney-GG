# Respresentation of spatial info
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Tree data structure
class Node():
    def __init__(self, x0, y0, w, h, points):
        self.x0 = x0
        self.y0 = y0
        self.w = w
        self.h = h
        self.points = points
        self.children = []

    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
    
    def get_points(self):
        return self.points


    #  Generate quadtree - top-down approach
    #  recursively divide node into 4 regions until threshold has been satisfied

    #  Stop division when each node contains less than k nodes
    def recursive_subdivide(node, k):
        if len(node.points)<=k:
            return
        
        w_ = float(node.width/2)
        h_ = float(node.height/2)

        p = contains(node.x0, node.y0, w_, h_, node.points)
        x1 = Node(node.x0, node.y0, w_, h_, p)
        recursive_subdivide(x1, k)

        p = contains(node.x0, node.y0+h_, w_, h_, node.points)
        x2 = Node(node.x0, node.y0+h_, w_, h_, p)
        recursive_subdivide(x2, k)

        p = contains(node.x0+w_, node.y0, w_, h_, node.points)
        x3 = Node(node.x0 + w_, node.y0, w_, h_, p)
        recursive_subdivide(x3, k)

        p = contains(node.x0+w_, node.y0+h_, w_, h_, node.points)
        x4 = Node(node.x0+w_, node.y0+h_, w_, h_, p)
        recursive_subdivide(x4, k)

        node.children = [x1, x2, x3, x4]

    
    def contains(x,y,w,h, points):
        pts = []
        for point in points:
            if point.x >=x and point.x <+ x+1 and point.y >= y and point.y <= y+h:
                pts.append(point)
        return pts

    def find_children(node):
        if not node.children:
            return [node]
        else:
            children = []
            for child in node.children:
                children += (find_children(child))
        return children
