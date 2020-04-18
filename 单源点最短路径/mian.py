
from manim_lib.imports import *
import copy
import heapq as q

class mian(My_Scene):

    def construct(self):

        self.begin_pic()
        self.beginning()
        self.part_01()
        self.part_02()
        self.part_03()

    def begin_pic(self):

        pic_0_pos='.\\..\\pic\\map.jpg'

        map_0=ImageMobject(pic_0_pos)

        map_0.set_height(8)

        self.play(FadeInFrom(map_0,UP))
        self.wait(1)

        pos_mark_round=Annulus(color=BLUE,inner_radius=0.3,outer_radius=0.7)
        pos_mark_spark=Triangle(color=BLUE,fill_opacity=1)
        pos_mark_spark.rotate(PI)
        pos_mark_spark.scale(0.6)
        pos_mark_spark.shift(DOWN*1.15)

        pos_mark=VGroup(pos_mark_round,pos_mark_spark)

        pos_mark.scale(0.3)

        pos_mark_1=pos_mark.copy()
        pos_mark_1.shift(UP+LEFT)

        self.play(FadeIn(pos_mark_1))

        self.wait(0.5)

        arr_line_1=Line(np.array([-1,1,0]),np.array([-0.5,1.5,0]),color=YELLOW)
        arr_line_2=Line(np.array([-0.5,1.5,0]),np.array([3.5,1.5,0]),color=YELLOW)
        you_e=TextMobject("你",color=YELLOW)
        you_e.move_to(np.array([4,1.5,0]))

        arr_l_1=VGroup(arr_line_1,arr_line_2,you_e)

        self.play(ShowCreation(arr_l_1))

        self.wait(1)

        pos_mark_2=pos_mark.copy()
        pos_mark_2.shift(DOWN+RIGHT*0.5)

        arr_line_3=Line(np.array([0.5,-1,0]),np.array([1,-0.5,0]),color=YELLOW)
        arr_line_4=Line(np.array([1,-0.5,0]),np.array([3,-0.5,0]),color=YELLOW)
        tar_e=TextMobject("目的地",color=YELLOW)
        tar_e.move_to(np.array([4,-0.5,0]))

        arr_l_2=VGroup(arr_line_3,arr_line_4,tar_e)

        self.play(FadeIn(pos_mark_2))
        
        self.wait(0.5)
        
        self.play(ShowCreation(arr_l_2))

        self.wait(1)

        # route_line_1=Line(np.array([-1,0.4,0]),np.array([-1.4,0.3,0]),color=RED)
        # route_line_2=Line(np.array([-1.4,0.3,0]),np.array([-1.35,-0.41,0]),color=RED)
        # route_line_3=Line(np.array([-1.35,-0.42,0]),np.array([0.15,-0.52,0]),color=RED)
        # route_line_4=Line(np.array([0.15,-0.5,0]),np.array([0.1,-1.7,0]),color=RED)
        # route_line_5=Line(np.array([0.1,-1.7,0]),np.array([0.5,-1.72,0]),color=RED)

        # route_1=VGroup(route_line_1,route_line_2,route_line_3,route_line_4,route_line_5)

        # self.play(ShowCreation(route_1))

        # self.wait(0.5)

        # cir_01=Circle(radius=0.7,color=RED)

        # cir_01.move_to(np.array([-1.2,0.35,0]))

        # fs_e=TextMobject("分手呜~",color=RED)

        # fs_mark=VGroup(cir_01,fs_e)

        # self.play(ShowCreation(fs_mark))

        # self.wait(1)

        # self.play(Uncreate(fs_mark),Uncreate(route_1),Uncreate(arr_l_2))

        pos_mark_everywhere=VGroup()

        for i in range(0,30):
            pos_mark_new=pos_mark.copy()
            pos_mark_new.move_to(np.array([(random.random()-0.5)*5,(random.random()-0.5)*8,0]))
            pos_mark_everywhere.add(pos_mark_new)

        self.play(FadeIn(pos_mark_everywhere))

        self.wait(1)

        self.play(Uncreate(pos_mark_everywhere),Uncreate(pos_mark_1),Uncreate(pos_mark_2),Uncreate(arr_l_1),FadeOutAndShiftDown(map_0),Uncreate(arr_l_2))

        self.wait(1)

    def beginning(self):

        title=TextMobject("单源点最短路径")
        author=TextMobject("by:泠妄")
        line=Line(buff=12,color=YELLOW)
        title.scale(2.5)
        title.shift(UP)
        author.shift(DOWN)

        self.play(ShowCreation(line))
        self.play(FadeInFrom(title,DOWN),FadeInFrom(author,UP))

        self.wait(1)

        self.play(FadeOut(line),FadeOutAndShift(author,UP),ApplyMethod(title.set_color,YELLOW))
        self.play(ApplyMethod(title.scale,0.55))
        self.play(ApplyMethod(title.to_edge,UP))

    def dfs_animate(self,gra_points,gra_edges,gra_length,gra_mobjects,gra,start,end,run_time=1,dis_scale=1,gra_dis_mobject=[],gra_dis_group=None):

        stack=[]
        edge_stack=[]
        while len(gra_dis_mobject)<len(gra_points):
            gra_dis_mobject.append(None)
        vis=[False for i in range(len(gra_points))]
        dis=[999999 for i in range(len(gra_points))]
        stack.append(start)
        vis[start]=True
        dis[start]=0
        s_now=[0 for i in range(len(gra_points))]

        while(len(stack)!=0):

            now=stack[len(stack)-1]
            #self.play(ApplyMethod(gra_mobjects[0][now].set_color,YELLOW,run_time=run_time))
            bre=False
            while s_now[now] < len(gra_edges):
                if gra_edges[s_now[now]][0]==now and not vis[gra_edges[s_now[now]][1]]:
                    self.play(ApplyMethod(gra_mobjects[0][now].set_color,YELLOW,run_time=run_time))
                    vis[gra_edges[s_now[now]][1]]=True
                    stack.append(gra_edges[s_now[now]][1])
                    edge_stack.append(s_now[now])
                    self.play(ApplyMethod(gra_mobjects[1][s_now[now]].set_color,YELLOW,run_time=run_time))

                    if len(gra_length)>s_now[now] and dis[gra_edges[s_now[now]][1]]>dis[now]+int(gra_length[s_now[now]]):
                        dis[gra_edges[s_now[now]][1]]=dis[now]+int(gra_length[s_now[now]])
                        gra_dis_mobject_new=TextMobject(str(dis[gra_edges[s_now[now]][1]]),color=YELLOW)
                        gra_dis_mobject_new.scale(dis_scale)
                        gra_dis_mobject_new.move_to(gra_points[gra_edges[s_now[now]][1]])
                        if gra_dis_mobject[gra_edges[s_now[now]][1]]==None:
                            gra_dis_mobject[gra_edges[s_now[now]][1]]=gra_dis_mobject_new
                            if gra_dis_group is not None:
                                gra_dis_group.add(gra_dis_mobject[gra_edges[s_now[now]][1]])
                            self.play(Write(gra_dis_mobject[gra_edges[s_now[now]][1]],run_time=run_time))
                        else:
                            self.play(Transform(gra_dis_mobject[gra_edges[s_now[now]][1]],gra_dis_mobject_new,run_time=run_time))
                            
                    bre=True
                    s_now[now]+=1
                    break
                s_now[now]+=1

            if not bre:
                stack.pop()
                vis[now]=False
                self.play(ApplyMethod(gra_mobjects[0][now].set_color,BLUE,run_time=run_time))
                if len(edge_stack)!=0:
                    self.play(ApplyMethod(gra_mobjects[1][edge_stack[len(edge_stack)-1]].set_color,BLUE,run_time=run_time))
                    edge_stack.pop()

    def bfs_animate(self,gra_points,gra_edges,gra_length,gra_mobjects,gra,start,end,run_time=1,dis_scale=1,gra_dis_mobject=[],gra_dis_group=None):

        queue=[]
        edge_queue=[]
        while len(gra_dis_mobject)<len(gra_points):
            gra_dis_mobject.append(None)
        vis=[False for i in range(len(gra_points))]
        dis=[999999 for i in range(len(gra_points))]
        queue.append(start)
        vis[start]=True
        dis[start]=0
        s_now=[0 for i in range(len(gra_points))]

        while(len(queue)!=0):

            now=queue[0]
            s_now[now]=0
            edg_add=0
            #self.play(ApplyMethod(gra_mobjects[0][now].set_color,YELLOW,run_time=run_time))
            while s_now[now] < len(gra_edges):
                if gra_edges[s_now[now]][0]==now:
                    self.play(ApplyMethod(gra_mobjects[0][now].set_color,YELLOW,run_time=run_time))
                    if  not vis[gra_edges[s_now[now]][1]]:
                        vis[gra_edges[s_now[now]][1]]=True
                        queue.append(gra_edges[s_now[now]][1])
                    

                    if len(gra_length)>s_now[now] and dis[gra_edges[s_now[now]][1]]>dis[now]+int(gra_length[s_now[now]]):
                        edge_queue.append(s_now[now])
                        self.play(ApplyMethod(gra_mobjects[1][s_now[now]].set_color,YELLOW,run_time=run_time))
                        edg_add+=1
                        dis[gra_edges[s_now[now]][1]]=dis[now]+int(gra_length[s_now[now]])
                        gra_dis_mobject_new=TextMobject(str(dis[gra_edges[s_now[now]][1]]),color=YELLOW)
                        gra_dis_mobject_new.scale(dis_scale)
                        gra_dis_mobject_new.move_to(gra_points[gra_edges[s_now[now]][1]])
                        if gra_dis_mobject[gra_edges[s_now[now]][1]]==None:
                            gra_dis_mobject[gra_edges[s_now[now]][1]]=gra_dis_mobject_new
                            if gra_dis_group is not None:
                                gra_dis_group.add(gra_dis_mobject[gra_edges[s_now[now]][1]])
                            self.play(Write(gra_dis_mobject[gra_edges[s_now[now]][1]],run_time=run_time))
                        else:
                            self.play(Transform(gra_dis_mobject[gra_edges[s_now[now]][1]],gra_dis_mobject_new,run_time=run_time))
                        
                s_now[now]+=1

            queue.pop(0)
            vis[now]=False
            self.play(ApplyMethod(gra_mobjects[0][now].set_color,BLUE,run_time=run_time))
            while len(edge_queue)!=0 and edg_add!=0:
                self.play(ApplyMethod(gra_mobjects[1][edge_queue[0]].set_color,BLUE,run_time=run_time))
                edge_queue.pop(0)
                edg_add-=1

    def part_01(self):

        def bfs_animate_c1(gra_points,gra_edges,gra_length,gra_mobjects,gra,start,end,run_time=1,dis_scale=1,gra_dis_mobject=[],gra_dis_group=None):

            queue=[]
            edge_queue=[]
            while len(gra_dis_mobject)<len(gra_points):
                gra_dis_mobject.append(None)
            vis=[False for i in range(len(gra_points))]
            dis=[999999 for i in range(len(gra_points))]
            queue.append(start)
            vis[start]=True
            dis[start]=0
            s_now=[0 for i in range(len(gra_points))]

            z_c_t=0
            z_c_t_w=None

            while(len(queue)!=0):

                now=queue[0]
                #self.play(ApplyMethod(gra_mobjects[0][now].set_color,YELLOW,run_time=run_time))
                while s_now[now] < len(gra_edges):
                    if gra_edges[s_now[now]][0]==now and not vis[gra_edges[s_now[now]][1]]:
                        self.play(ApplyMethod(gra_mobjects[0][now].set_color,YELLOW,run_time=run_time))
                        vis[gra_edges[s_now[now]][1]]=True
                        queue.append(gra_edges[s_now[now]][1])
                        edge_queue.append(s_now[now])
                        self.play(ApplyMethod(gra_mobjects[1][s_now[now]].set_color,YELLOW,run_time=run_time))

                        if len(gra_length)>s_now[now] and dis[gra_edges[s_now[now]][1]]>dis[now]+int(gra_length[s_now[now]]):
                            dis[gra_edges[s_now[now]][1]]=dis[now]+int(gra_length[s_now[now]])
                            gra_dis_mobject_new=TextMobject(str(dis[gra_edges[s_now[now]][1]]),color=YELLOW)
                            gra_dis_mobject_new.scale(dis_scale)
                            gra_dis_mobject_new.move_to(gra_points[gra_edges[s_now[now]][1]])
                            if gra_dis_mobject[gra_edges[s_now[now]][1]]==None:
                                gra_dis_mobject[gra_edges[s_now[now]][1]]=gra_dis_mobject_new
                                if gra_dis_group is not None:
                                    gra_dis_group.add(gra_dis_mobject[gra_edges[s_now[now]][1]])
                                self.play(Write(gra_dis_mobject[gra_edges[s_now[now]][1]],run_time=run_time))
                            else:
                                self.play(Transform(gra_dis_mobject[gra_edges[s_now[now]][1]],gra_dis_mobject_new,run_time=run_time))
                            if gra_edges[s_now[now]][1]==end:
                                if z_c_t==0:
                                    z_c_t_w=TextMobject("它现在并不是最小值！",color=RED)
                                    z_c_t_w.move_to(gra_points[end])
                                    z_c_t_w.shift(RIGHT*1.5+DOWN)
                                    self.play(Write(z_c_t_w),run_time=0.5)
                                elif z_c_t==1:
                                    z_c_t_w_t1=TextMobject("仍然不是",color=RED)
                                    z_c_t_w_t1.move_to(z_c_t_w.get_center())
                                    self.play(Transform(z_c_t_w,z_c_t_w_t1))
                                elif z_c_t==2:
                                    z_c_t_w_t2=TextMobject("舒服了",color=BLUE)
                                    z_c_t_w_t2.move_to(z_c_t_w.get_center())
                                    self.play(Transform(z_c_t_w,z_c_t_w_t2))
                                
                                z_c_t+=1
                            
                    s_now[now]+=1

                queue.pop(0)
                vis[now]=False
                self.play(ApplyMethod(gra_mobjects[0][now].set_color,BLUE,run_time=run_time))
                if len(edge_queue)!=0:
                    self.play(ApplyMethod(gra_mobjects[1][edge_queue[0]].set_color,BLUE,run_time=run_time))
                    edge_queue.pop(0)

            return z_c_t_w

        gra_1_ori_mobject=[]
        gra_1_points=[np.array([-3,0,0]),np.array([-1.5,2,0]),np.array([0,1,0]),np.array([0,-1,0]),np.array([2,1.5,0]),np.array([2,-0.5,0])]
        gra_1_edges=[(0,5),(0,2),(0,3),(2,5),(0,1),(1,4),(4,5),(4,2)]
        gra_1_length=["8","3","5","2","1","2","1","1"]

        gra_1_ori=self.draw_graphe(0,0.5,gra_1_ori_mobject,
        points=gra_1_points,
        edges=gra_1_edges,
        length=gra_1_length
        )


        gra_1_1=gra_1_ori.copy()
        gra_1_1_mobject=copy.deepcopy(gra_1_ori_mobject)

        dis_mobject=[]
        dis_mobject_group=VGroup()

        self.play(ShowCreation(gra_1_1))

        self.wait(1)

        tt=TextMobject("DFS",color=RED)
        tt.shift(RIGHT*3+UP*2)

        self.play(Write(tt))

        self.dfs_animate(gra_1_points,gra_1_edges,gra_1_length,gra_1_1_mobject,gra_1_1,0,5,0.1,1,dis_mobject,dis_mobject_group)

        self.wait(0.5)

        self.play(FadeOut(dis_mobject_group))
        dis_mobject.clear()
        dis_mobject_group=VGroup()

        tt_t=TextMobject("BFS",color=RED)
        tt_t.shift(RIGHT*3+UP*2)

        self.play(Transform(tt,tt_t))

        self.bfs_animate(gra_1_points,gra_1_edges,gra_1_length,gra_1_1_mobject,gra_1_1,0,5,0.1,1,dis_mobject,dis_mobject_group)

        self.wait(1)

        self.play(FadeOut(dis_mobject_group))

        z_c_t=bfs_animate_c1(gra_1_points,gra_1_edges,gra_1_length,gra_1_1_mobject,gra_1_1,0,5,0.5,1,dis_mobject,dis_mobject_group)

        self.play(FadeOut(dis_mobject_group),FadeOutAndShiftDown(gra_1_1),Uncreate(z_c_t),Uncreate(tt))

        for i in gra_1_1_mobject:
            for j in i:
                self.play(FadeOutAndShiftDown(j,run_time=0.01))

    def part_02(self):

        begin_text=TextMobject("n个点？",coloe=YELLOW)
        begin_text.scale(2)

        self.play(Write(begin_text))
        self.wait(1)
        self.play(FadeOutAndShiftDown(begin_text))

        gra_2_ori_mobject=[]
        gra_2_points=[np.array([-5.5,0,0]),np.array([-4.3,1.5,0]),np.array([-3.8,-0.5,0]),
        np.array([-4,-2,0]),np.array([-3,0.5,0]),np.array([-1,-2,0]),np.array([-0.5,0.4,0]),
        np.array([1,1,0]),np.array([2,-1,0]),np.array([2.5,1,0]),
        np.array([3.6,-1,0]),np.array([4,0.5,0])]
        gra_2_edges=[(0,1),(0,2),(1,2),(0,3),(1,6),(1,7),(2,4),(2,5),(2,6),(3,5),(4,6),(5,6),(6,7),(7,9),(7,8),(7,10),(8,10),(9,10),(9,11),(10,11)]
        gra_2_length=["3","2","2","1","3","8","1","1","3","1","1","3","2","3","1","2","3","1","4","2"]

        gra_2_ori=self.draw_graphe(0,0.3,gra_2_ori_mobject,
        points=gra_2_points,
        edges=gra_2_edges,
        length=gra_2_length)

        self.play(ShowCreation(gra_2_ori))

        self.wait(0.5)

        dis_mobject=[]
        dis_mobject_group=VGroup()
        
        self.bfs_animate(gra_2_points,gra_2_edges,gra_2_length,gra_2_ori_mobject,gra_2_ori,0,5,0.01,1,dis_mobject,dis_mobject_group)

        self.wait(1)

        xn_t=TextMobject("来n遍？",color=YELLOW)
        xn_t.shift(RIGHT*3+DOWN*2)

        self.play(Write(xn_t))

        self.wait(1)

        surr_1=Rectangle(width=12,height=5,color=YELLOW,fill_opacity=0)

        self.play(ShowCreationThenDestruction(surr_1))

        xn_t_t1=TextMobject("已经好了，不需要",color=YELLOW)
        xn_t_t1.move_to(xn_t.get_center())

        self.wait(0.5)
        self.play(Transform(xn_t,xn_t_t1))

        self.wait(1)

        cover_1=FullScreenRectangle(color=BLACK,fill_opacity=0.6)

        time_use_1=TextMobject("$\\theta =(N)$?",color=BLUE)
        time_use_1.scale(2)

        self.play(FadeIn(cover_1),Write(time_use_1))

        self.wait(1)

        wrong_1_1=Rectangle(height=0.4,width=3,color=RED,fill_opacity=1)
        wrong_1_1.rotate(PI/4)
        wrong_1_2=Rectangle(height=0.4,width=3,color=RED,fill_opacity=1)
        wrong_1_2.rotate(PI*3/4)

        wrong_1=VGroup(wrong_1_1,wrong_1_2)

        self.play(FadeIn(wrong_1))

        self.wait(1)

        self.play(FadeOut(wrong_1),FadeOut(cover_1),FadeOut(time_use_1),FadeOut(xn_t),FadeOut(dis_mobject_group))

        dis_mobject_group=VGroup()
        dis_mobject.clear()

        sqre_1=Rectangle(height=3,width=4,color=YELLOW,fill_opacity=0)
        sqre_1.shift(RIGHT*2.6)

        self.wait(0.5)
        self.play(ShowCreation(sqre_1))

        self.bfs_animate(gra_2_points,gra_2_edges,gra_2_length,gra_2_ori_mobject,gra_2_ori,0,5,0.1,1,dis_mobject,dis_mobject_group)

        self.wait(0.5)

        xn_t2=TextMobject("$\\theta =(E*N)$",color=BLUE)
        xn_t2.scale(2)

        self.play(FadeIn(cover_1),Write(xn_t2))

        self.wait(1)

        bell_name_t=TextMobject("Bellman-Ford",color=BLUE)
        bell_name_t.scale(2)

        self.play(ReplacementTransform(xn_t2,bell_name_t))

        self.wait(1)

        self.play(FadeOut(cover_1),Uncreate(bell_name_t),Uncreate(sqre_1),FadeOut(dis_mobject_group))

        for i in gra_2_ori_mobject:
            for j in i:
                self.play(FadeOut(j,run_time=0.01))

        self.wait(1)

    def dji(self,gra_points,gra_edges,gra_length,gra_mobjects,gra,start,run_time=1,dis_scale=1,gra_dis_mobject=[],gra_dis_group=None):
        
        que=[]
        while len(gra_dis_mobject)<len(gra_points):
            gra_dis_mobject.append(None)
        vis=[False for i in range(len(gra_points))]
        vis[0]=True
        dis=[999999 for i in range(len(gra_points))]
        dis[0]=0
        q.heappush(que,[0,start])

        while(len(que)!=0):
            
            now_q=(q.heappop(que))
            now=now_q[1]

            self.play(ApplyMethod(gra_mobjects[0][now].set_color,RED,run_time=run_time))

            for i in range(len(gra_edges)):
                if gra_edges[i][0]==now:
                    self.play(ApplyMethod(gra_mobjects[1][i].set_color,YELLOW,run_time=run_time))
                    if dis[gra_edges[i][1]]>dis[now]+int(gra_length[i]):
                        self.play(ApplyMethod(gra_mobjects[0][gra_edges[i][1]].set_color,YELLOW,run_time=run_time))
                        dis[gra_edges[i][1]]=dis[now]+int(gra_length[i])
                        q.heappush(que,[dis[gra_edges[i][1]],gra_edges[i][1]])
                        gra_dis_mobject_new=TextMobject(str(dis[gra_edges[i][1]]),color=YELLOW)
                        gra_dis_mobject_new.scale(dis_scale)
                        gra_dis_mobject_new.move_to(gra_points[gra_edges[i][1]])
                        if gra_dis_mobject[gra_edges[i][1]]==None:
                            gra_dis_mobject[gra_edges[i][1]]=gra_dis_mobject_new
                            if gra_dis_group is not None:
                                gra_dis_group.add(gra_dis_mobject[gra_edges[i][1]])
                            self.play(Write(gra_dis_mobject[gra_edges[i][1]],run_time=run_time))
                        else:
                            self.play(Transform(gra_dis_mobject[gra_edges[i][1]],gra_dis_mobject_new,run_time=run_time))

                    self.play(ApplyMethod(gra_mobjects[1][i].set_color,BLUE,run_time=run_time))

    def part_03(self):
        why_t=TextMobject("为什么喵？")
        why_t.scale(2)

        self.play(Write(why_t))

        self.wait(1)

        res_t_1=TextMobject("dis[i]非最小\\\\dis[i]+w非最小")

        self.play(ReplacementTransform(why_t,res_t_1))

        self.wait(1)

        self.play(Uncreate(res_t_1))

        gra_r1_mobject=[]
        gra_r1_points=[np.array([-5,0,0]),
        np.array([-3,2,0]),np.array([-3,0,0]),np.array([-3,-2,0]),
        np.array([-1,2,0]),np.array([-1,-2,0]),np.array([-1,-0.7,0]),np.array([-1,0.7,0]),
        np.array([1,2,0]),np.array([1,-2,0]),np.array([1,0,0]),
        np.array([3,0,0])]
        gra_r1_edges=[(0,1),(0,2),(1,2),(0,3),(1,6),(1,7),(2,4),(2,5),(2,6),(3,5),(4,6),(5,6),(6,7),(7,9),(7,8),(7,10),(8,10),(9,10),(9,11),(10,11)]
        gra_r1_length=["3","2","2","1","3","8","1","1","3","1","1","3","2","3","1","2","3","1","4","2"]

        gra_r1=self.draw_graphe(0,0.3,gra_r1_mobject,
        points=gra_r1_points,
        edges=gra_r1_edges,
        length=gra_r1_length)

        fts_t=CurvedArrow(np.array([-1+0.3,2,0]),np.array([-1+0.3,-0.7,0]),color=BLUE)
        fts_t.flip()
        fts_t.shift(RIGHT*0.6)
        # self.play(ShowCreation(fts_t))
        gra_r1.remove(gra_r1_mobject[1][10])
        gra_r1_mobject[1][10]=fts_t
        gra_r1.add(gra_r1_mobject[1][10])
        gra_r1_mobject[2][10].shift(RIGHT+UP*0.1)
        self.wait(0.5)
        self.play(ShowCreation(gra_r1))

        self.play(ApplyMethod(gra_r1_mobject[1][1].set_color,RED),ApplyMethod(gra_r1_mobject[1][6].set_color,RED),ApplyMethod(gra_r1_mobject[1][10].set_color,RED))

        surr_1=Rectangle(height=5,width=1,color=YELLOW)
        surr_1.shift(LEFT)

        self.wait(1)
        self.play(ShowCreationThenDestruction(surr_1))

        self.wait(1)

        surr_2=Rectangle(height=5,width=3.5,color=YELLOW)
        surr_2.shift(RIGHT*2)

        self.play(ShowCreationThenDestruction(surr_2,run_time=2))

        cover_1=FullScreenRectangle(color=BLACK,fill_opacity=0.7)

        self.wait(1)

        self.play(FadeIn(cover_1))

        dis_t=TextMobject("距离")
        dis_t.scale(2)

        self.play(Write(dis_t))

        self.wait(1)

        self.play(Uncreate(dis_t),FadeOut(cover_1))

        gra_r2_mobject=[]
        gra_r2_points=[np.array([-6.5,0,0]),
        np.array([-2,1.5,0]),np.array([-3.5,1.5,0]),np.array([-5,0,0]),
        np.array([-2,-1.5,0]),np.array([-3.5,-1.5,0]),np.array([-0.5,0,0]),
        np.array([0.7,0,0]),
        np.array([1.9,0,0]),np.array([4.3,0,0]),np.array([3.1,0,0]),
        np.array([5.5,0,0])]
        gra_r2_edges=[(0,1),(0,2),(1,2),(0,3),(1,6),(1,7),(2,4),(2,5),(2,6),(3,5),(4,6),(5,6),(6,7),(7,9),(7,8),(7,10),(8,10),(9,10),(9,11),(10,11)]
        gra_r2_length=["3","2","2","1","3","8","1","1","3","1","1","3","2","3","1","2","3","1","4","2"]

        gra_r2=self.draw_graphe(0,0.3,gra_r2_mobject,
        points=gra_r2_points,
        edges=gra_r2_edges,
        length=gra_r2_length)

        self.wait(0.5)

        stn_t=CurvedArrow(gra_r2_points[7]+np.array([0,1.15,0]),gra_r2_points[9]+np.array([0,1.15,0]),color=BLUE)
        stn_t.flip(RIGHT)
        gra_r2.remove(gra_r2_mobject[1][13])
        gra_r2_mobject[1][13]=stn_t
        gra_r2.add(gra_r2_mobject[1][13])
        gra_r2_mobject[2][13].shift(UP)

        stt_t=CurvedArrow(gra_r2_points[7]+np.array([0,-0.3,0]),gra_r2_points[10]+np.array([0,-0.3,0]),color=BLUE)
        gra_r2.remove(gra_r2_mobject[1][15])
        gra_r2_mobject[1][15]=stt_t
        gra_r2.add(gra_r2_mobject[1][15])
        gra_r2_mobject[2][15].shift(DOWN)

        tte_t=CurvedArrow(gra_r2_points[10]+np.array([0,-0.3,0]),gra_r2_points[11]+np.array([0,-0.3,0]),color=BLUE)
        gra_r2.remove(gra_r2_mobject[1][19])
        gra_r2_mobject[1][19]=tte_t
        gra_r2.add(gra_r2_mobject[1][19])
        gra_r2_mobject[2][19].shift(DOWN)

        self.play(ReplacementTransform(gra_r1,gra_r2))

        self.wait(1)

        self.play(ApplyMethod(gra_r2_mobject[0][1].set_color,YELLOW),ApplyMethod(gra_r2_mobject[1][2].set_color,RED),ApplyMethod(gra_r2_mobject[1][4].set_color,RED),ApplyMethod(gra_r2_mobject[1][5].set_color,RED))

        self.wait(1)

        self.play(ApplyMethod(gra_r2_mobject[0][1].set_color,BLUE),ApplyMethod(gra_r2_mobject[1][2].set_color,BLUE),ApplyMethod(gra_r2_mobject[1][4].set_color,BLUE),ApplyMethod(gra_r2_mobject[1][5].set_color,BLUE))

        self.wait(1)

        unknown_t=TextMobject("未知的点")
        unknown_t.shift(RIGHT*0.7)
        unknown_c=Circle(radius=0.3,color=BLUE,fill_opacity=0)
        unknown_c.shift(LEFT)

        unknown=VGroup(unknown_t,unknown_c)
        unknown.shift(UP)

        known_t=TextMobject("已知的点")
        known_t.shift(RIGHT*0.7)
        known_c=Circle(radius=0.3,color=YELLOW,fill_opacity=0)
        known_c.shift(LEFT)

        known=VGroup(known_c,known_t)

        begin_t=TextMobject("出发过的点")
        begin_t.shift(RIGHT*0.7)
        begin_c=Circle(radius=0.3,color=RED,fill_opacity=0)
        begin_c.shift(LEFT)

        begin=VGroup(begin_t,begin_c)
        begin.shift(DOWN)

        exp_gt=VGroup(unknown,known,begin)

        exp_gt.to_edge(RIGHT)
        exp_gt.shift(UP*2.5)

        self.play(ShowCreation(exp_gt))

        gra_r2_dis_mobject=[]
        gra_r2_dis_mobject_group=VGroup()

        self.dji(gra_r2_points,gra_r2_edges,gra_r2_length,gra_r2_mobject,gra_r2,0,0.3,1,gra_r2_dis_mobject,gra_r2_dis_mobject_group)

        self.wait(1)

        time_1=TextMobject("$\\theta (N)$")
        time_2=TextMobject("$*\\theta (N)$")

        time_1.scale(2)
        time_1.shift(LEFT*1.4)
        time_2.scale(2)
        time_2.shift(RIGHT*1.6)

        time_all=VGroup(time_1,time_2)

        self.play(FadeIn(cover_1),Write(time_1))
        self.wait(1)
        self.play(Write(time_2))

        self.wait(1)

        time_all_t=TextMobject("$\\theta (N^2)$")
        time_all_t.scale(2)

        self.play(Transform(time_all,time_all_t))

        self.wait(1)

        cover_2=cover_1.deepcopy()

        dui_t_1=TextMobject("堆")
        dui_t_1.to_corner(UP+LEFT)
        dui_t_1.shift(RIGHT+DOWN)

        dui_exp=TextMobject("c++:queue->priority\\_queue\\\\python:heapq\\\\java:priority\\_queue")

        self.play(FadeIn(cover_2),Write(dui_t_1),Write(dui_exp))

        dui_exp_2=TextMobject("obj->堆->最值\\\\$\\theta (logN)$")

        dui_exp_2.to_edge(DOWN)
        dui_exp_2.shift(UP*1.5)

        self.wait(0.5)
        self.play(Write(dui_exp_2))

        gra_neg=self.draw_graphe(-1,0.5,
        points=[np.array([0,2,0]),np.array([2,0,0]),np.array([0,-2,0]),np.array([-2,0,0])],
        edges=[(0,1),(1,2),(2,3),(3,0)],
        length=['-1','-1','-1','-1'])

        time_all_t2=TextMobject("$\\theta (E+N)log(N)$")
        time_all_t2.scale(2)

        self.wait(1)

        self.play(FadeOut(cover_2),Uncreate(dui_exp),Uncreate(dui_exp_2),Uncreate(dui_t_1))

        self.wait(0.5)

        self.play(Transform(time_all,time_all_t2))

        self.wait(1)

        self.play(FadeOut(cover_1),Uncreate(time_all))

        self.wait(1)

        self.play(ReplacementTransform(gra_r2,gra_neg),FadeOut(gra_r2_dis_mobject_group),FadeOut(exp_gt))

        self.wait(1)

        self.play(FadeOut(gra_neg))
    