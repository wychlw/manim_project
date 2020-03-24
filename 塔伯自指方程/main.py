from manimlib.imports import *
import math
from functools import reduce

from manimlib.imports import *

class MyText_old(TexMobject):

    CONFIG = {
        'default_font': '阿里巴巴普惠体',
    }

    def __init__(self, *tex_strings, **kwargs):
        self.tex_list = tex_strings
        TexMobject.__init__(self, *tex_strings, **kwargs)
        self.not_replace_texs = ['\\over', ]
        self.new_font_texs = VGroup()

    def reset_tex_with_font(self):
        self.new_font_texs = VGroup()

    def get_color_by_tex(self, tex, **kwargs):
        parts = self.get_parts_by_tex(tex, **kwargs)
        colors = []
        for part in parts:
            colors.append(part.get_color())
        return colors[0]

    def set_font_by_tex(self, tex, font, new_tex=None, color=None, **kwargs):
        parts_to_font = self.get_parts_by_tex(tex, **kwargs)
        if color == None:
            color = self.get_color_by_tex(tex)

        if new_tex != None:
            tex = new_tex
        for part in parts_to_font:

            tex_new = Text(tex, font=font, color=color)
            tex_new.set_height(part.get_height())
            # tex_new.set_width(part.get_width())
            tex_new.move_to(part)
            self.new_font_texs.add(tex_new)

    def set_font_by_tex_to_font_map(self, texs_to_font_map, texs_replace_map, **kwargs):
        for texs, font in list(texs_to_font_map.items()):
            try:
                # If the given key behaves like tex_strings
                if texs in texs_replace_map:
                    self.set_font_by_tex(texs, font, new_tex=texs_replace_map[texs], **kwargs)
                else:
                    self.set_font_by_tex(texs, font, **kwargs)
            except TypeError:
                # If the given key is a tuple
                for tex in texs:
                    if tex in texs_replace_map:
                        self.set_font_by_tex(texs, font, new_tex=texs_replace_map[texs], **kwargs)
                    else:
                        self.set_font_by_tex(texs, font, **kwargs)

    def create_default_font_dict(self):
        self.default_font_dict = {}
        for tex in self.tex_strings:
            if not tex in self.not_replace_texs:
                self.default_font_dict[tex] = self.default_font
        return self.default_font_dict

    def get_new_font_texs(self, texs_replace_map, **kwargs):
        texs_to_font_map = self.create_default_font_dict()
        self.set_font_by_tex_to_font_map(texs_to_font_map, texs_replace_map, **kwargs)
        return self.new_font_texs

class MyText(TexMobject):

    CONFIG = {
        'default_font': '阿里巴巴普惠体',
        'tex_scale_factor': 1,
    }

    def __init__(self, *tex_strings, **kwargs):
        self.tex_list = tex_strings
        TexMobject.__init__(self, *tex_strings, **kwargs)
        self.new_font_texs = VGroup()

    def reset_tex_with_font(self):
        self.new_font_texs = VGroup()

    def get_color_by_tex(self, tex, **kwargs):
        parts = self.get_parts_by_tex(tex, **kwargs)
        colors = []
        for part in parts:
            colors.append(part.get_color())
        return colors[0]

    def get_new_font_texs(self, replace_dict):
        for i in range(len(self.tex_strings)):
            tex = self.tex_strings[i]
            color=self.get_color_by_tex(tex)
            if tex in replace_dict:
                tex = replace_dict[tex]
            tex_new = Text(tex, font=self.default_font, color=color)
            tex_new.set_height(self[i].get_height())
            if tex == '-' or tex == '=':
                tex_new.set_width(self[i].get_width(), stretch=True)
            tex_new.scale(self.tex_scale_factor)
            tex_new.move_to(self[i])
            self.new_font_texs.add(tex_new)
        return self.new_font_texs

class my_scene(Scene):
        

    def func(self,**kwargs):

        k = 4858450636189713423582095962494202044581400587983244549483093085061934704708809928450644769865524364849997247024915119110411605739177407856919754326571855442057210445735883681829823754139634338225199452191651284348332905131193199953502413758765239264874613394906870130562295813219481113685339535565290850023875092856892694555974281546386510730049106723058933586052544096664351265349363643957125565695936815184334857605266940161251266951421550539554519153785457525756590740540157929001765967965480064427829131488548259914721248506352686630476300
        mod = 17
        x_r=106
        y_r=17

        def f(x,y):
            d = (((-mod) * x) - (y % mod))
            e = reduce(lambda x,y: x*y, [2 for x in range(-d)]) if d else 1
            f = ((y // mod) // e)
            g = f % 2
            return 0.5 < g
        
        if 'k' in kwargs.keys():
            k=kwargs['k']
        if 'mod' in kwargs.keys():
            mod=kwargs['mod']
        if 'x_r' in kwargs.keys():
            x_r=kwargs['x_r']
        if 'y_r' in kwargs.keys():
            y_r=kwargs['y_r']

        for y in range(k+y_r-1, k-1, -1):

            for x in range(0, x_r+1):

                if f(x,y):
                    self.points.append((x,y-k))

    points=[]

    def d(self,**kwargs):

        self.points.clear()
        self.func(**kwargs)

        x_mid=107/2
        y_mid=17/2
        gou=VGroup()

        for i in self.points:

            sqr=Square(side_length=0.08,color=RED,fill_opacity=1)

            sqr.shift(np.array([(i[0]-x_mid)*0.1,(i[1]-y_mid)*0.1,0]))

            gou.add(sqr)

        x_axis=NumberLine(x_min=-6.2,x_max=6.2,color=BLUE)

        x_str=TexMobject("x",color=BLUE)

        x_str.next_to(x_axis.get_corner(RIGHT+DOWN))

        x_axis.add(x_str)
        
        for i in range(-1,12):

            num=TexMobject(str(i*10))

            num.shift(np.array([(i-5)-0.3,-0.3,0]))

            x_axis.add(num)

        x_axis.shift(np.array([-0.5,-1,0]))

        gou.add(x_axis)

        y_axis=NumberLine(x_min=-1.5,x_max=1.5,color=BLUE)
        y_axis.rotate(np.pi / 2, about_point=y_axis.number_to_point(0))

        y_str=TexMobject("y",color=BLUE)

        y_str.next_to(y_axis.get_corner(LEFT+TOP))

        y_axis.add(y_str)

        for i in range(1,3):

            num=TexMobject("k+"+str(i*10))

            num.shift(np.array([-0.5,(i-1),0]))

            y_axis.add(num)

        y_axis.shift(LEFT*5.5)

        gou.add(y_axis)
        gou.shift(DOWN)

        return gou

    def zm_proc(self,text):

        zm=TextMobject(text)
        zm.scale(0.5)
        zm.to_edge(DOWN)
        return zm

    def construct(self):
        
        zm=self.zm_proc("这是一个有些复杂的方程")

        func0=TextMobject("$\\frac{1}{2} < \\lfloor $mod$ (\\lfloor\\frac{y}{5}\\rfloor 2^{-5\\lfloor x \\rfloor - \\text{mod} (\\lfloor y \\rfloor\\text{,} 5 )}\\text{,} 2 )\\rfloor$",color=BLUE)

        self.play(Write(func0),Write(zm))
        
        self.wait(1)

        love=179057560799192115125

        lov=self.d(k=love,mod=5,x_r=13,y_r=5)

        self.play(ApplyMethod(func0.to_edge,UP))

        arr0=Arrow(func0.get_corner(LEFT+DOWN),lov.get_top()+LEFT*3,color=BLUE)

        cond0=TextMobject("$0 \\leq x \\leq 13$ , $k \\leq y \\leq k+5$",color="#BBFFFF")
        k_val0=TextMobject("其中，k=179057560799192115125",color="#BBFFFF")

        cond0.next_to(arr0.get_edge_center(RIGHT))
        cond0.shift(RIGHT*0.5)
        k_val0.scale(0.7)
        k_val0.next_to(cond0.get_bottom())
        k_val0.shift(LEFT*4+DOWN*0.3)

        zm2=self.zm_proc("当x属于0，13的一个闭区间，y属于k，k+5的一个闭区间时，它的解集相当适合理科生表白(k等于上面的那一坨)")

        self.play(Transform(zm,zm2),ShowCreation(lov),ShowCreation(arr0),ShowCreation(cond0),ShowCreation(k_val0))

        self.wait(1)

        zm3=self.zm_proc("可它最出名的却并非这个形式")

        func1=TextMobject("$\\frac{1}{2} < \\lfloor \\text{mod} (\\lfloor\\frac{y}{17}\\rfloor 2^{-17\\lfloor x \\rfloor - \\text{mod} (\\lfloor y \\rfloor\\text{,} 17 )}\\text{,} 2 )\\rfloor$",color=BLUE)

        func1.to_edge(UP)

        cond1=TextMobject("$0 \\leq x \\leq 106$ , $k \\leq y \\leq k+17$",color="#BBFFFF")
        k_val1=TextMobject("其中,k=485845063618971342358209596249420204458...",color="#BBFFFF")
        sor=TextMobject("对不起这个k实在是太大了...这里真的放不下...我把它丢到最后面去了...",color="#BBFFFF")

        cond1.next_to(arr0.get_edge_center(RIGHT))
        cond1.shift(RIGHT*0.5)
        k_val1.scale(0.7)
        k_val1.next_to(cond1.get_bottom())
        k_val1.shift(LEFT*4+DOWN*0.3)
        sor.scale(0.5)
        sor.next_to(cond1.get_bottom())
        sor.shift(DOWN*0.8+LEFT*5)

        it_self0=self.d()

        self.play(Transform(zm,zm3))

        self.wait(1)

        zm4=self.zm_proc("将方程变换一下，当x属于0，106的一个闭区间，y属于k，k+17的一个闭区间时，它就是它自身")

        self.play(Transform(zm,zm4))
        self.play(Transform(func0,func1),Transform(cond0,cond1),Transform(k_val0,k_val1),Transform(lov,it_self0),Write(sor))

        self.wait(1)

        zm5=self.zm_proc("可是，这是为什么？")
        self.play(Transform(zm,zm5))

        self.wait(1)
        zm6=self.zm_proc("-")

        self.play(Transform(zm,zm6),FadeOut(func0),FadeOut(cond0),FadeOut(k_val0),FadeOut(lov),FadeOut(sor),FadeOut(arr0))
        

        title=TextMobject("塔珀自指公式")
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
        """

        zm=self.zm_proc("-")
        self.play(Write(zm))
        """
        func_p1=TexMobject("\\frac{1}{2}<",color="#00FFFF")
        func_p2_b=TexMobject("\\text{mod(}",color="#00FFFF")
        func_p3=TexMobject("\\lfloor\\frac{y}{n}\\rfloor",color="#00FFFF")
        func_p4=TexMobject("2^{-n\\lfloor x\\rfloor-\\text{mod}(\\lfloor y\\rfloor ,n)}",color="#00FFFF")
        func_p2_e=TexMobject("\\text{,2)}",color="#00FFFF")

        func_p2_b.next_to(func_p3.get_right())
        func_p2_b.shift(LEFT*2.5)
        func_p1.next_to(func_p2_b.get_right())
        func_p1.shift(LEFT*2.5)
        func_p4.next_to(func_p3.get_left())
        func_p4.shift(RIGHT*0.6)
        func_p2_e.next_to(func_p4.get_left())
        func_p2_e.shift(RIGHT*3.5)

        func_form=VGroup(func_p3,func_p4)
        func_p2=VGroup(func_p2_b,func_p2_e)
        func_right=VGroup(func_form,func_p2)
        func_full=VGroup(func_p1,func_right)

        zm7=self.zm_proc("让我们来仔细观察一下这个式子")

        self.play(Transform(zm,zm7),Write(func_full))

        self.wait(1)

        zm8=self.zm_proc("先来处理一下右边里面这一大坨")

        self.play(Transform(zm,zm8),FadeOutAndShiftDown(func_p1),FadeOutAndShiftDown(func_p2))
        self.play(ApplyMethod(func_form.shift,LEFT*2.5),ApplyMethod(func_form.scale,2))

        self.wait(1)

        zm9=self.zm_proc("简单的变个形")

        func_p4_t1=TexMobject("\\frac{1}{2^{n\\lfloor x\\rfloor+\\text{mod}(\\lfloor y\\rfloor ,n)}}",color="#00FFFF")

        func_p4_t1.points=func_p4.points
        func_p4_t1.scale(1.5)
        func_p4_t1.shift(RIGHT*1.5+UP*0.2)

        self.play(Transform(zm,zm9),Transform(func_p4,func_p4_t1))
        self.wait(1)

        func_p4_t2=TexMobject("\\frac{ }{2^{n\\lfloor x\\rfloor+\\text{mod}(\\lfloor y\\rfloor ,n)}}",color="#00FFFF")

        func_p4_t2.points=func_p4_t1.points
        func_p4_t2.scale(2.5)

        self.play(Transform(func_p4,func_p4_t2),ApplyMethod(func_p3.shift,UP+RIGHT*1.4))
        self.play(ApplyMethod(func_p4.shift,DOWN*0.8))

        self.wait(1)

        zm10=self.zm_proc("我们容易发现，在给定的范围内，$\\lfloor\\frac{y}{n}\\rfloor$恒为一个常数")

        xz=TexMobject("y\\in[k,k+n]",color="#00EEEE")
        surr_p3=Rectangle(hight=5,width=2,color=YELLOW)
        con=TextMobject("const",color="#7AC5CD")

        con.next_to(func_p3.get_right())
        con.shift(RIGHT)
        surr_p3.shift(LEFT*0.5+UP)
        xz.to_edge(RIGHT)
        xz.shift(UP)

        self.play(Transform(zm,zm10),Write(xz),Write(con))

        self.wait(0.5)
        self.play(ShowCreation(surr_p3))
        self.wait(0.5)
        self.play(Uncreate(surr_p3))

        self.wait(1)

        zm11=self.zm_proc("于是，我们用B来代替")

        func_p3_t1=TextMobject("B",color="#00FFFF")

        func_p3_t1.scale(2.5)
        func_p3_t1.shift(UP*0.6+LEFT*0.5)

        self.play(Transform(zm,zm11),Transform(func_p3,func_p3_t1),FadeOut(xz),FadeOut(con))

        self.wait(1)

        zm12=self.zm_proc("而关于下面这一部分，先让我们看另外一个东西")

        surr_p4=Rectangle(htgit=2.5,width=10,color=YELLOW)

        surr_p4.shift(DOWN*0.8)

        self.play(Transform(zm,zm12),ShowCreation(surr_p4))
        self.wait(0.5)
        self.play(Uncreate(surr_p4))
        self.wait(1)
        self.play(FadeOutAndShiftDown(func_form))
        self.wait(0.5)
        

        bit_1=TextMobject("1",color="#FFF68F")
        bit_2=TextMobject("0",color="#FFF68F")
        bit_3=TextMobject("1",color="#FFF68F")
        bit_4=TextMobject("1",color="#FFF68F")

        bit_1.scale(1.5)
        bit_2.scale(1.5)
        bit_3.scale(1.5)
        bit_4.scale(1.5)
        bit_1.shift(LEFT*3+UP)
        bit_2.shift(LEFT*1+UP)
        bit_3.shift(RIGHT*1+UP)
        bit_4.shift(RIGHT*3+UP)

        binary=VGroup(bit_1,bit_2,bit_3,bit_4)
        
        zm13=self.zm_proc("这是一个二进制数")

        self.play(Transform(zm,zm13),ShowCreation(binary))
        self.wait(1)

        zm14=self.zm_proc("它可以用这样一种方法转化为10进制")

        trans_1=TextMobject("$1*2^3$",color="#66CD00")
        trans_2=TextMobject("$0*2^2$",color="#66CD00")
        trans_3=TextMobject("$1*2^1$",color="#66CD00")
        trans_4=TextMobject("$1*2^0$",color="#66CD00")

        add_1=TextMobject("+",color="#66CD00")
        add_2=TextMobject("+",color="#66CD00")
        add_3=TextMobject("+",color="#66CD00")
        equ=TextMobject("=",color="#66CD00")
        ans=TextMobject("11",color="#66CD00")

        trans_1.shift(np.array([-3,-0.5,0]))
        trans_2.shift(np.array([-1,-0.5,0]))
        trans_3.shift(np.array([1,-0.5,0]))
        trans_4.shift(np.array([3,-0.5,0]))

        add_1.shift(np.array([-2,-0.5,0]))
        add_2.shift(np.array([0,-0.5,0]))
        add_3.shift(np.array([2,-0.5,0]))
        equ.shift(np.array([4,-0.5,0]))
        ans.shift(np.array([4.5,-0.5,0]))

        rep=VGroup(trans_1,trans_2,trans_3,trans_4,add_1,add_2,add_3,equ,ans)

        self.play(Transform(zm,zm14),Write(rep))
        self.wait(1)

        zm15=self.zm_proc("当我们将其向左移一位，我们可以发现，数字变大了$2^1$倍")
        bit_new=TextMobject("0",color="#FFF68F")
        trans_new=TextMobject("$1*2^4$",color="#66CD00")
        trans_1_t=TextMobject("$0*2^3$",color="#66CD00")
        trans_2_t=TextMobject("$1*2^2$",color="#66CD00")
        trans_3_t=TextMobject("$1*2^1$",color="#66CD00")
        trans_4_t=TextMobject("$0*2^0$",color="#66CD00")
        add_new=TextMobject("+",color="#66CD00")
        ans_new=TextMobject("22",color="#66CD00")

        bit_new.scale(1.5)
        trans_1_t.shift(np.array([-3,-0.5,0]))
        trans_2_t.shift(np.array([-1,-0.5,0]))
        trans_3_t.shift(np.array([1,-0.5,0]))
        trans_4_t.shift(np.array([3,-0.5,0]))
        bit_new.shift(np.array([3,1,0]))
        trans_new.shift(np.array([-5,-0.5,0]))
        add_new.shift(np.array([-4,-0.5,0]))
        ans_new.shift(np.array([4.5,-0.5,0]))

        self.play(Transform(zm,zm15),ApplyMethod(binary.shift,LEFT*2),Write(bit_new))
        self.play(Write(add_new),Write(trans_new),Transform(trans_1,trans_1_t),Transform(trans_2,trans_2_t),Transform(trans_3,trans_3_t),Transform(trans_4,trans_4_t),Transform(ans,ans_new))
        self.wait(1)

        binary.add(bit_new)
        rep.add(add_new,trans_new)

        b_t=TextMobject("num",color="#FFF68F")
        l_s_oper=TextMobject("<<",color="#EEC591")
        x_tt=TextMobject("x",color="#EED8AE")

        b_t.scale(1.5)
        l_s_oper.scale(2)
        x_tt.scale(2)

        b_t.shift(np.array([-1,0,0]))
        l_s_oper.shift(np.array([0.2,0,0]))
        x_tt.shift(np.array([1,0,0]))

        b_s=VGroup(b_t,l_s_oper,x_tt)
        b_s.shift(UP)

        t_t=TextMobject("num",color="#FF7F50")
        t_oper=TextMobject("*",color="#F08080")
        p_x=TextMobject("$2^x$",color="#FF8C00")

        t_t.scale(1.5)
        t_oper.scale(2)
        p_x.scale(2)

        t_t.shift(np.array([-1,0,0]))
        t_oper.shift(np.array([0.2,0,0]))
        p_x.shift(np.array([1,0,0]))

        t_s=VGroup(t_t,t_oper,p_x)
        t_s.shift(DOWN)

        arr_b_t=Arrow(b_s.get_bottom(),t_s.get_top(),color="#FFFFE0")

        zm16=self.zm_proc("事实上，我们每左移x位，数字就变大$2^x$倍")

        self.play(Transform(zm,zm16),ReplacementTransform(binary,b_s),ReplacementTransform(rep,t_s),ShowCreation(arr_b_t))
        self.wait(1)

        zm17=self.zm_proc("那反过来，每除以$2^x$,就是向右移了x位")

        l_s_oper_t=TextMobject(">>",color="#EEC591")
        l_s_oper_t.scale(2)
        l_s_oper_t.shift(np.array([0.2,1,0]))

        t_oper_t=TextMobject("/",color="#F08080")
        t_oper_t.scale(2)
        t_oper_t.shift(np.array([0.2,-1,0]))

        arr_t_b=Arrow(t_s.get_top(),b_s.get_bottom(),color="#FFFFE0")

        self.play(Transform(zm,zm17),Transform(l_s_oper,l_s_oper_t),Transform(t_oper,t_oper_t),ReplacementTransform(arr_b_t,arr_t_b))
        self.wait(1)
        
        zm18=self.zm_proc("现在，让我们回到原来的式子")
        self.play(Transform(zm,zm18),FadeOut(arr_t_b),FadeOut(l_s_oper),FadeOut(t_oper),Uncreate(t_s),Uncreate(b_s),Uncreate(binary))
        

        func_p3_2=TexMobject("B",color="#00FFFF")
        func_p4_2=TexMobject("\\frac{ }{2^{n\\lfloor x\\rfloor+\\text{mod}(\\lfloor y\\rfloor ,n)}}",color="#00FFFF")

        func_p3_2.scale(2.5)
        func_p4_2.scale(1.5)
        func_p3_2.shift(UP*0.5)
        func_p4_2.shift(DOWN*0.5)

        func_f=VGroup(func_p3_2,func_p4_2)

        self.play(Write(func_f))

        self.wait(1)

        zm19=self.zm_proc("套用刚才的公式，我们继续将式子变形")

        self.play(Transform(zm,zm19))

        self.play(ApplyMethod(func_p3_2.shift,LEFT*3.5),ApplyMethod(func_p4_2.shift,RIGHT*1.5))

        func_p4_2_t1=TexMobject(">> n\\lfloor x\\rfloor+\\text{mod}(\\lfloor y\\rfloor ,n)",color="#00FFFF")
        
        func_p4_2_t1.scale(1.5)
        func_p4_2_t1.shift(np.array([1,0,0]))

        self.play(Transform(func_p4_2,func_p4_2_t1),ApplyMethod(func_p3_2.shift,DOWN*0.5))

        self.wait(1)

        zm20=self.zm_proc("我们暂时把它叫做g(x)")

        g_x=TexMobject("g(x)",color="#00FFFF")

        func_l=TexMobject("\\frac{1}{2} <",color="#00FFFF")

        func_m_l=TexMobject("\\text{mod}(",color="#00FFFF")

        func_m_r=TexMobject("\\text{,} 2 )",color="#00FFFF")

        func_l.shift(np.array([-2.5,0,0]))
        func_m_l.shift(np.array([-1.25,0,0]))
        g_x.shift(np.array([0,0,0]))
        func_m_r.shift(np.array([1,0,0]))

        func_m=VGroup(func_m_l,func_m_r)

        self.play(Transform(zm,zm20),Transform(func_f,g_x),Write(func_l),Write(func_m))

        self.wait(1)

        surr_m=Rectangle(height=1,width=4,color=YELLOW)

        zm21=self.zm_proc("又由于，右边这个式子的结果只可能是0或1\\\\(不懂mod的可以去看看以前的一期？)")

        equ_2=TexMobject("=",color=RED)

        ans_2=TexMobject("0 / 1",color="#48D1CC")

        equ_2.rotate(TAU/4)

        equ_2.move_to(surr_m.get_center())
        equ_2.shift(UP)
        ans_2.move_to(equ_2.get_center())
        ans_2.shift(UP*0.6)

        self.play(Transform(zm,zm21),ShowCreation(surr_m))
        self.play(Write(equ_2))
        self.play(Write(ans_2))

        self.wait(1)

        zm22=self.zm_proc("于是，整个式子就变成了：判断g(x)是奇数还是偶数")

        judg=TextMobject("判断$g(x)$\\\\是奇数还是偶数",color="#00FFFF")
        
        judg.shift(RIGHT*2)

        self.play(Transform(zm,zm22),ApplyMethod(func_f.shift,LEFT*2),Uncreate(surr_m),Uncreate(equ_2),Uncreate(ans_2),Uncreate(func_l),Uncreate(func_m),Write(judg))
        self.wait(1)

        zm23=self.zm_proc("刚刚我们用了二进制，那这里呢？")

        sep=DashedLine(np.array([0,2.5,0]),np.array([0,0.5,0]))

        self.play(Transform(zm,zm23),ShowCreation(sep),ApplyMethod(func_f.shift,UP),ApplyMethod(judg.shift,UP))

        self.wait(1)

        zm24=self.zm_proc("事实上，所有奇数的二进制末位为1，偶数的二进制末位为0")

        odd=TextMobject("奇数: ... 1",color="#EEE685")
        eve=TextMobject("偶数: ... 0",color="#EEE685")

        odd.scale(1.5)
        eve.scale(1.5)
        odd.shift(LEFT*2+DOWN)
        eve.shift(RIGHT*2+DOWN)

        self.play(Transform(zm,zm24),Write(odd),Write(eve))
        self.wait(1)

        zm25=self.zm_proc("所以，整个式子相当于：判断g(x)末位是0还是1")

        judg_t=TextMobject("判断$g(x)$\\\\末位是0还是1",color="#00FFFF")

        judg_t.shift(UP+RIGHT*2)

        self.play(Transform(zm,zm25),Transform(judg,judg_t))

        self.wait(1)

        zm26=self.zm_proc("现在我们来感受一下,它究竟在做什么")

        func_fin_l=TexMobject("B",color="#00FFFF")
        func_fin_r=TexMobject(">> n\\lfloor x\\rfloor+\\text{mod}(\\lfloor y\\rfloor ,n)",color="#00FFFF")

        func_fin_l.shift(LEFT*2.5)
        func_fin_r.shift(RIGHT*0.5)
        func_fin=VGroup(func_fin_l,func_fin_r)

        func_fin.shift(LEFT*2)

        self.play(Transform(zm,zm26),Uncreate(odd),Uncreate(eve),Uncreate(sep),ReplacementTransform(func_f,func_fin),ApplyMethod(judg.shift,DOWN+RIGHT*2))
        self.wait(1)
        self.play(ApplyMethod(func_fin.shift,np.array([-2,0,0])),Uncreate(judg))

        sepr=DashedLine(np.array([0,2,0]),np.array([0,-3,0]))

        sepr.shift(LEFT*0.5)

        x_axis=NumberLine(x_min=-7,x_max=7,stroke_width=2,color=BLUE)
        y_axis=NumberLine(x_min=-3,x_max=3,stroke_width=2,color=BLUE)

        x_t=TexMobject("x",color=BLUE)
        y_t=TexMobject("y",color=BLUE)

        y_axis.rotate(TAU/4)
        x_axis.shift(np.array([0,-2,0]))
        y_axis.shift(np.array([-6,0,0]))
        x_t.next_to(x_axis.get_corner(RIGHT+DOWN))
        x_t.scale(1.5)
        y_t.next_to(y_axis.get_corner(UP+LEFT))
        y_t.scale(1.5)
        y_t.shift(LEFT*0.5)

        axis=VGroup(x_axis,y_axis,x_t,y_t)

        axis.scale(0.5)
        axis.shift(np.array([3,0,0]))

        self.play(ShowCreation(sepr),ShowCreation(axis))

        y_net=[]
        x_net=[]
        net=VGroup()
        
        for i in range(0,5):
            line_new=Line(np.array([-3.5,0,0]),np.array([3.3,0,0]),stroke_width=0.7,color=BLUE)
            line_new.shift(RIGHT*3.5+DOWN*0.45)
            line_new.shift(UP*(i*0.5))
            y_net.append(line_new)
            net.add(y_net[i])

        for i in range(0,13):
            line_new=Line(np.array([0,-1,0]),np.array([0,1.7,0]),stroke_width=0.7,color=BLUE)
            line_new.shift(RIGHT*0.65)
            line_new.shift(RIGHT*(i*0.5))
            x_net.append(line_new)
            net.add(x_net[i])

        self.play(ShowCreation(net))
        self.wait(1)

        poi=[]

        for i in range(0,14):
            iop=[]
            for j in range(0,6):
                iop.append(np.array([0.15+0.5*i,-0.95+0.5*j,0]))
            poi.append(iop)

        zm27=self.zm_proc("为了简单,这里以ILY为示例，并将x、y限制为整数")

        func_fin_r_t1=TexMobject(">> 5x + \\text{mod} (y\\text{,} 5 )",color="#00FFFF")

        requ=TexMobject("x,y\\in N\\\\x\\in [0,13) , y\\in [k,k+5)",color="#00FFFF")
        
        requ.shift(UP*1.5+LEFT*3.5)
        func_fin_r_t1.move_to(func_fin_r.get_center())

        self.play(Transform(zm,zm27),Transform(func_fin_r,func_fin_r_t1),Write(requ))
        self.wait(1)

        self.points.clear()
        self.func(k=love,mod=5,x_r=13,y_r=5)

        zm28=self.zm_proc("从(0,k)到(0,k+4),右边式子的结果由0变到了5\\\\而B的后5位正好是1 0 0 0 1")

        surr_rt=Rectangle(width=6,height=1.2,color=YELLOW)

        surr_rt.move_to(func_fin.get_center())
        surr_rt.shift(RIGHT*0.3)

        anse=TexMobject("-",color=BLUE)

        anse.move_to(func_fin.get_bottom()+DOWN*1.5)


        poip=[1,0,0,0,1]
        show=[]
        count=0
        pic=VGroup()

        self.play(Transform(zm,zm28),ShowCreation(surr_rt))

        for i in range(0,5):
            anse_n=TextMobject("B >> "+str(i)+" = "+str(poip[i]))
            anse_n.move_to(anse.get_center())
            self.play(Transform(anse,anse_n))
            if (0,i) in self.points:
                cir=Circle(radius=0.05,color=YELLOW)
                cir.move_to(poi[0][i])
                show.append(cir)
                pic.add(show[count])
                self.play(FadeIn(show[count]))
                count=count+1
        
        self.wait(1)
        
        zm29=self.zm_proc("而当$x=2$时,式子结果又变为了6到10")

        self.play(Transform(zm,zm29))

        poip_2=[1,1,1,1,1]

        for i in range(0,5):
            anse_n=TextMobject("B >> "+str(i+5)+" = "+str(poip_2[i]))
            anse_n.move_to(anse.get_center())
            self.play(Transform(anse,anse_n))
            if (1,i) in self.points:
                cir=Circle(radius=0.05,color=YELLOW)
                cir.move_to(poi[1][i])
                show.append(cir)
                pic.add(show[count])
                self.play(FadeIn(show[count]))
                count=count+1

                self.wait(1)

        zm30=self.zm_proc("接下来,我们继续这样遍历完整个网格")
        pic_2=VGroup()

        for j in range(2,13):
            for i in range(0,5):
                if (j,i) in self.points:
                    cir=Circle(radius=0.05,color=YELLOW)
                    cir.move_to(poi[j][i])
                    show.append(cir)
                    pic_2.add(show[count])
                    count=count+1

        pic.add(pic_2)

        self.play(Transform(zm,zm30),FadeOut(anse),ShowCreation(pic_2))

        self.wait(1)

        zm31=self.zm_proc("而当我们去除正整数的限制时，我们相当于填满了整个格子")

        func_fin_r_t2=TexMobject(">> n\\lfloor x\\rfloor+\\text{mod}(\\lfloor y\\rfloor ,n)",color="#00FFFF")
        requ_t1=TexMobject("x\\in [0,13) , y\\in [k,k+5)",color="#00FFFF")

        func_fin_r_t2.move_to(func_fin_r_t1.get_center())
        requ_t1.move_to(requ.get_center())

        self.play(Transform(zm,zm31),Transform(func_fin_r,func_fin_r_t2),Transform(requ,requ_t1))
        self.wait(0.5)

        show_squ=[]
        pic_squ=VGroup()
        count_squ=0

        for j in range(0,13):
            for i in range(0,5):
                if (j,i) in self.points:
                    squ=Square(side_length=0.5,fill_opacity=1,color=YELLOW)
                    squ.move_to(poi[j][i]+np.array([0.25,0.25,0]))
                    show_squ.append(squ)
                    pic_squ.add(show_squ[count_squ])
                    count_squ=count_squ+1

        self.play(ReplacementTransform(pic,pic_squ))

        self.wait(1)

        self.play(Uncreate(func_fin),Uncreate(axis),Uncreate(sepr),Uncreate(requ),Uncreate(pic_squ),Uncreate(surr_rt),Uncreate(net))

        zm32=self.zm_proc("那,B又是怎么来的?")

        B_t=TexMobject("B",color="#20B2AA")
        B_r=TexMobject("?",color="#20B2AA")

        B_t.scale(2)
        B_r.scale(2)
        B_t.shift(LEFT*0.3)
        B_r.shift(RIGHT*0.3)

        self.play(Transform(zm,zm32),Write(B_t),Write(B_r))
        self.wait(1)

        zm33=self.zm_proc("(见图)")

        K_e=TextMobject("k=B*n \\text{(n为图像的高度)",color="#20B2AA")
        B_r_t=TextMobject(":图像每列连起来的二进制",color="#20B2AA")

        K_e.scale(2)
        K_e.shift(UP*1.5)
        B_r_t.scale(2)
        B_r_t.shift(RIGHT*0.4)

        self.play(Transform(zm,zm33),ApplyMethod(B_t.shift,LEFT*5.8),Transform(B_r,B_r_t),Write(K_e))
        self.wait(1)

        self.play(Uncreate(B_t),Uncreate(B_r),Uncreate(K_e))
        self.wait(1)

        