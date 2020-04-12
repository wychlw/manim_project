from manimlib.imports import *

class  My_Graphe(Scene):

    def draw_graphe(self,start_point,rad,mobject=[],**kwargs):
        """
        points: np.array

        edge: (start_point,end_point)

        length: str

        mobject: an array used to store every mobject incase you may want to change it
            however, it is not must required.
        """

        gra=VGroup()
        points=()
        points_mobject=[]
        length=()
        length_mobject=[]
        edges=()
        edges_mobject=[]

        if "points" in kwargs:
            points=kwargs["points"]

        if "edges" in kwargs:
            edges=kwargs["edges"]
        
        if "length" in kwargs:
            length=kwargs["length"]

        for i in range(len(points)):

            cir_new=Circle(color=BLUE,radius=rad)
            cir_new.move_to(points[i])

            if i==start_point:
                s=TextMobject("s",color=BLUE)
                s.scale(rad/0.3)
                s.move_to(points[i])
                cir_new.add(s)
            
            points_mobject.append(cir_new)
            gra.add(points_mobject[i])
            

        for i in range(len(edges)):

            a=points[edges[i][0]][0]-points[edges[i][1]][0]
            b=points[edges[i][0]][1]-points[edges[i][1]][1]
            c=math.sqrt(a*a+b*b)
            rad_minus=np.array([a*(rad/c),b*(rad/c),0])
            edge_new=Line(points[edges[i][0]]-rad_minus,points[edges[i][1]]+rad_minus,color=BLUE)
            edge_new.add_tip(0.25)
            edges_mobject.append(edge_new)
            gra.add(edges_mobject[i])

            if i<len(length):
                length_new=TextMobject(length[i],color=YELLOW)
                length_new.move_to((points[edges[i][0]]+points[edges[i][1]])/2)
                length_mobject.append(length_new)
                gra.add(length_mobject[i])
            
        mobject.append(points_mobject)
        mobject.append(edges_mobject)
        mobject.append(length_mobject)

        return gra