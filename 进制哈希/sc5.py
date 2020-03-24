from manimlib.imports import *

class MyText_old(TexMobject):

    CONFIG = {
        'default_font': '思源黑体',
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
        'default_font': 'SWGothe',
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

class my_scene2(Scene):

    def construct(self):

        title=TextMobject("进制哈希")
        sur=Rectangle(color=BLUE)

        title.scale(2)
        sur.surround(title)

        self.play(FadeIn(title),ShowCreation(sur))
        self.wait(1)

        self.play(FadeOut(sur),ApplyMethod(title.to_edge,UP))
        self.wait(1)

        define=TextMobject("模除:",color=YELLOW)
        fp=TextMobject("a/b=n$\\dots$",color=GREEN)
        ys=TextMobject("c",color=GREEN)
        div=VGroup(fp,ys)

        fp.scale(1.5)
        ys.scale(1.5)
        ys.next_to(fp,RIGHT)
        ys.shift(DOWN*0.05)
        define.to_corner(LEFT+UP)
        define.shift(DOWN*2,RIGHT*0.5)
        define.scale(1.1)
        div.shift(UP*0.5)

        self.play(FadeInFrom(define,DOWN))
        self.play(Write(div))
        self.wait(0.5)

        kk=Rectangle(color=BLUE)
        kk.surround(ys)
        kk.scale(1.5)
        str_mod="a"+"\\%"+"b=c"
        mod=TextMobject(str_mod,color=BLUE)
        mod.scale(1.5)
        mod.shift(DOWN*0.5)
        arr=Arrow(kk.get_bottom(),mod.get_right())

        self.play(ShowCreation(kk),FadeInFrom(arr,DOWN),Write(mod))
        self.wait(1)

        fw=TextMobject("c$\\in\\lbrack$0,b$)\\quad\\cap\\quad$c$\\in$Z",color=BLUE)
        fw.scale(1.2)

        fw.shift(DOWN*1.5)
        md=VGroup(mod,fw)

        self.play(Write(fw))
        self.wait(0.5)
        self.play(FadeOut(arr),FadeOut(div),FadeOut(kk))
        self.play(ApplyMethod(md.shift, UP))
        self.wait(0.5)
        self.play(FadeOut(define),FadeOutAndShiftDown(md))
        self.wait(0.5)

        ff=TextMobject("如可直接将其转化到对应的Ascii值")

        self.play(Write(ff))
        self.wait(0.5)
        self.play(FadeOut(ff))

        dy=TextMobject("\'a\' $\\to$ 1$\\quad$\'b\' $\\to$ 2",color=BLUE)
        str1=TextMobject("\"ab\"",color=BLUE)
        neq=TextMobject("$\\neq$",color=BLUE)
        str2=TextMobject("\"ba\"",color=BLUE)
        t1=TextMobject("1+2=3",color=BLUE)
        t2=TextMobject("2+1=3",color=BLUE)
        eq=TextMobject("=",color=BLUE)
        dy.scale(1.5)
        str1.scale(1.5)
        neq.scale(1.5)
        str2.scale(1.5)
        t1.scale(1.5)
        t2.scale(1.5)
        eq.scale(1.5)

        dy.shift(UP*3)
        str1.shift(LEFT*3,UP*1.5)
        str2.shift(RIGHT*3,UP*1.5)
        neq.shift(UP*1.5)
        t1.shift(LEFT*3,DOWN*1)
        t2.shift(RIGHT*3,DOWN*1)
        eq.shift(DOWN*1)

        arr1=Arrow(str1,t1)
        arr2=Arrow(str2,t2)

        gou=VGroup(dy,str1,neq,str2,arr1,arr2,t1,eq,t2)
        gou.shift(DOWN)

        self.play(Write(dy))
        self.play(FadeIn(str1),FadeIn(str2))
        self.play(FadeIn(neq),FadeInFromDown(arr1),FadeInFromDown(arr2))
        self.play(Write(t1),Write(t2))
        self.play(FadeIn(eq))

        err=TextMobject("ERR",color=RED)
        err.scale(6)
        err.shift(DOWN)

        self.wait(0.5)
        self.play(FadeIn(err))
        self.wait(0.5)
        self.play(FadeOut(err),FadeOut(gou))

        obo=TextMobject("\'c1\'\\%c$\\oplus$\'c2\'\\%c$\\oplus$\'c3\'\\%c$\\oplus\\dots\\oplus$\'cn\'\\%c")
        exp=TextMobject("$\\oplus$：某种合并的方式")
        exp.shift(DOWN)
        self.play(Write(obo))
        self.play(Write(exp))
        self.wait(1)
        self.play(FadeOut(obo),FadeOut(exp))

        self.wait(0.5)

        title2=TextMobject("进制",color=YELLOW)
        title2.scale(2)
        title2.to_edge(UP)

        self.play(Transform(title,title2))

        sub_title=TextMobject("十进制")
        sub_title.scale(1.5)

        tt=TextMobject("十位数",color="#E6E6FA")
        ot=TextMobject("个位数",color="#E6E6FA")

        tn=TextMobject("3",color="#E6E6FA")
        on=TextMobject("8",color="#E6E6FA")

        cal=TextMobject("*10$\\quad$+",color="#E6E6FA")
        res=TextMobject("=38",color="#E6E6FA")

        tt.scale(1.5)
        ot.scale(1.5)
        tn.scale(1.5)
        on.scale(1.5)
        cal.scale(1.5)
        res.scale(1.5)

        sub_title.shift(UP*2.2)

        tt.shift(UP,LEFT*2)
        ot.shift(UP,RIGHT*2)
        tn.shift(DOWN,LEFT*2)
        on.shift(DOWN,RIGHT*2)
        cal.shift(DOWN)
        res.next_to(on.get_right(),RIGHT)

        self.play(FadeInFrom(sub_title,DOWN))
        self.play(FadeIn(tt),FadeIn(ot))
        self.play(Write(tn),Write(on))
        self.wait(0.5)
        self.play(Write(cal))
        self.play(Write(res))
        self.wait(1)

        sub_title2=TextMobject("n进制？")
        sub_title2.scale(1.5)
        sub_title2.shift(UP*2.2)
        
        self.play(Transform(sub_title,sub_title2),FadeOut(res))

        cal2=TextMobject("*n$\\quad$+",color="#E6E6FA")
        cal2.scale(1.5)
        cal2.shift(DOWN)

        self.wait(0.5)
        self.play(Transform(cal,cal2))
        self.wait(1)
        self.play(FadeOut(cal),FadeOut(sub_title),FadeOut(tt),FadeOut(ot),FadeOut(tn),FadeOut(on))

        title_r=TextMobject("进制哈希")
        title_r.scale(2)
        title_r.to_edge(UP)

        self.play(Transform(title,title_r))

        obo1=TextMobject("\'c1\'\\%c")
        obo2=TextMobject("$\\oplus$")
        obo3=TextMobject("\'c2\'\\%c$\\oplus$\'c3\'\\%c$\\oplus\\dots\\oplus$\'cn\'\\%c")

        obo1.scale(1.5)
        obo2.scale(1.5)
        obo3.scale(1.5)

        obo2.next_to(obo1.get_right())
        obo3.next_to(obo2.get_right())

        surr1=Rectangle(color=BLUE)

        gou2=VGroup(obo1,obo2,obo3)

        gou2.shift(UP+LEFT*5)

        surr1.surround(obo1)

        surr2=Rectangle(hight=surr1.get_height(),width=10,color=BLUE)
        surr2.shift(UP+RIGHT*2)

        exp1=TextMobject("十位数")
        exp2=TextMobject("个位数")

        exp1.scale(1.3)
        exp2.scale(1.3)

        exp1.shift(DOWN*2)
        exp2.shift(DOWN*2)

        exp1.shift(LEFT*2)
        exp2.shift(RIGHT*2)

        s1te1=Arrow(surr1.get_bottom(),exp1.get_top(),color=BLUE)
        s2te2=Arrow(surr2.get_bottom(),exp2.get_top(),color=BLUE)

        self.play(Write(gou2))

        self.play(ShowCreation(surr1),ShowCreation(surr2))

        title_c=TextMobject("进制哈希",color=YELLOW)
        title_c.scale(2)
        title_c.to_edge(UP)

        self.play(FadeIn(s1te1),FadeIn(s2te2),FadeInFromDown(exp1),FadeInFromDown(exp2))
        self.wait(1)

        self.play(Transform(title_r,title_c))

        self.wait(0.5)
        self.play(FadeOut(gou2),FadeOut(surr1),FadeOut(surr2),FadeOut(s1te1),FadeOut(s2te2),FadeOut(exp1),FadeOut(exp2))

        code=TextMobject("for each char in string:\\\\$\\quad\\quad\\quad\\quad\\quad\\quad\\quad\\quad\\quad$hash = (( hash * base ) + char ) \\% mod",color=RED)

        self.play(Write(code))
        self.wait(1)
        self.play(FadeOut(code))

        self.wait(1)

        notice1=TextMobject("1、尽量不要选取合数")
        notice2=TextMobject("2、尽量选择大质数")
        eg=TextMobject("eg: 1e9+7 \\& 1e9+9",color=YELLOW)

        notice1.scale(1.5)
        notice1.shift(UP*1.5)
        notice2.scale(1.5)
        notice2.shift(DOWN)
        eg.shift(DOWN*2.5)

        self.play(Write(notice1))
        self.wait(0.5)
        self.play(Write(notice2))
        self.wait(0.5)
        self.play(FadeIn(eg))
        self.wait(1)

        self.play(FadeOut(title),FadeOut(title_r),FadeOut(notice1),FadeOut(notice2),FadeOut(eg))