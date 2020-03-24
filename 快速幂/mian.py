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

class my_scene3(Scene):

    def construct(self):

        mi=TextMobject("$a^b$",color=BLUE)

        zm1=TextMobject("相信大家对幂运算都不陌生")

        mi.scale(3)
        zm1.to_edge(DOWN)

        self.play(Write(mi),Write(zm1))

        self.wait(1.5)

        mi2=TextMobject("$114514^{1919810}$",color=BLUE)

        zm2=TextMobject("但如果我们要算的数字很大的时候，我们又该如何算呢？")

        zmp=TextMobject("答案会放在最后的")

        mi2.scale(3)
        zm2.to_edge(DOWN)
        zmp.shift(DOWN*2)

        self.play(Transform(mi,mi2),Transform(zm1,zm2),Write(zmp))

        self.wait(2)

        self.play(FadeOut(mi),FadeOut(zm1),FadeOut(zmp))

        title=TextMobject("快速幂算法")
        author=TextMobject("by:泠妄")
        line=Line(length=20,color=YELLOW)
        title.scale(2.5)
        title.shift(UP)
        author.shift(DOWN)

        self.play(ShowCreation(line))
        self.play(FadeInFrom(title,DOWN),FadeInFrom(author,UP))

        self.wait(1)

        self.play(FadeOut(line),FadeOutAndShift(author,UP),ApplyMethod(title.set_color,YELLOW))
        self.play(ApplyMethod(title.scale,0.65))
        self.play(ApplyMethod(title.to_edge,UP))
        
        zm3=TextMobject("对此，我们要用到幂运算的一个性质")
        mi3=TextMobject("$a^b$",color=BLUE)

        mi3.scale(3)
        zm3.to_edge(DOWN)

        self.play(Write(mi3),Write(zm3))
        self.wait(0.5)

        gs=TextMobject("$=a^{(x+y)}$",color=BLUE)
        exp=TextMobject("(x+y=b)",color=BLUE)

        gs.scale(3)
        exp.shift(DOWN*1.5)
        gs.shift(RIGHT*1.5)

        self.play(ApplyMethod(mi3.shift,LEFT*2))
        self.play(Write(gs),Write(exp))

        self.wait(1.5)

        gs2=TextMobject("$=a^x \\bullet a^y$",color=BLUE)

        gs2.scale(3)
        gs2.shift(RIGHT*2)

        self.play(Transform(gs,gs2))

        self.wait(2.5)

        zm4=TextMobject("为了减少运算的次数，我们可令x=y=$\\frac{a}{2}$，则")

        exp2=TextMobject("(x=$\\frac{a}{2}$)",color=BLUE)
        gs3=TextMobject("$={(a^x)}^2$",color=BLUE)

        gs3.scale(3)
        exp2.shift(DOWN*1.5)
        gs3.shift(RIGHT*1.2)
        zm4.to_edge(DOWN)

        self.play(Transform(zm3,zm4),Transform(exp,exp2),Transform(gs,gs3))

        self.wait(4)

        zm5=TextMobject("但是，我们发现，当b为奇数时，会出现非整数幂的情况")
        eg1=TextMobject("$a^5=a^{2.5}*a^{2.5}$",color=RED)

        eg1.scale(2)
        eg1.shift(DOWN*2.5)
        zm5.to_edge(DOWN)

        self.play(Transform(zm3,zm5),FadeIn(eg1))
        self.wait(4)

        zm6=TextMobject("所以，我们对公式进行一些完善")

        gou_fun=VGroup(gs,exp,mi3)

        func=TextMobject("$a^b=\\begin{cases} a^x\\bullet a^x\\quad (a\\%2=0,x=\\frac{a}{2}) \\\\ a^x\\bullet a^x\\bullet a\\quad (a\\%2=1,x=\\frac{a-1}{2})\\end{cases}$",color=BLUE)

        zm6.to_edge(DOWN)
        func.scale(1.5)

        self.play(FadeOut(eg1),Transform(zm3,zm6))
        self.play(Transform(gou_fun,func))

        self.wait(3)

        zm7=TextMobject("接下来，我们只需继续递归的解决即可")

        zm7.to_edge(DOWN)

        self.play(Transform(zm3,zm7))

        self.wait(0.5)

        self.play(FadeOut(gou_fun))

        self.wait(1)

        zm8=TextMobject("但由于计算出来的结果很大\\\\一般来说，我们会要求将结果取余")

        fun=TextMobject("$a^b \\% c$",color=BLUE)

        fun.scale(3)
        zm8.to_edge(DOWN)

        self.play(Transform(zm3,zm8),Write(fun))

        self.wait(2)

        zm9=TextMobject("那我们又要继续对公式进行更改")

        zm9.to_edge(DOWN)

        self.play(Transform(zm3,zm9))
        self.wait(0.5)
        self.play(FadeOut(fun))

        gs4=TextMobject("$(A \\star B) \\% m = ((A \\% m) \\star (B \\% m))\\% m$",color=BLUE)
        zm10=TextMobject("还好，模除有一些公式，非常有用")

        zm10.to_edge(DOWN)

        self.play(Transform(zm3,zm10),Write(gs4))

        self.wait(3)

        gs5=TextMobject("$a^b\\% m=\\begin{cases} (a^x\\bullet a^x)\\% m\\quad (a\\%2=0,x=\\frac{a}{2}) \\\\ (a^x\\bullet a^x\\bullet a)\\% m\\quad (a\\%2=1,x=\\frac{a-1}{2})\\end{cases}$",color=BLUE)
        zm11=TextMobject("于是")

        zm11.to_edge(DOWN)

        self.play(Transform(zm3,zm11))
        self.play(Transform(gs4,gs5))
        self.wait(2)

        gs6=TextMobject("$a^b\\% m=\\begin{cases} (a^x\\% m)\\bullet (a^x\\% m)\\% m\\quad (a\\%2=0,x=\\frac{a}{2}) \\\\ (a^x\\% m)\\bullet (a^x\\bullet a\\% m)\\% m\\quad (a\\%2=1,x=\\frac{a-1}{2})\\end{cases}$",color=BLUE)

        self.play(Transform(gs4,gs6))

        self.wait(3)

        zm12=TextMobject("这种方法节省的时间还是非常可观的")

        tra=TextMobject("传统连乘时间复杂度:$\\Theta $(N)",color=YELLOW)
        ksm=TextMobject("快速幂时间复杂度:$\\Theta $(logN)",color=YELLOW)

        tra.scale(2)
        ksm.scale(2)
        tra.shift(UP)
        ksm.shift(DOWN)
        zm12.to_edge(DOWN)

        self.play(Transform(zm3,zm12),FadeOut(gs4))
        self.play(Write(tra))
        self.play(Write(ksm))
        self.wait(1.5)

        zm13=TextMobject("上一波代码")

        zm13.to_edge(DOWN)

        self.play(Transform(zm3,zm13),FadeOutAndShiftDown(tra),FadeOutAndShiftDown(ksm))

        
        code=TextMobject('while(b > 0)\\\\$\\lbrace$\\\\    if(b \\% 2 == 1)\\\\    $\\lbrace$\\\\        ans *= base;',color=GREEN,alignment="")
        code2=TextMobject("        ans \\%= m;\\\\    $\\rbrace$\\\\    base *= base;\\\\    base \\%= m;\\\\    b /= 2;\\\\ $\\rbrace$",color=GREEN,alignment="")

        code.shift(LEFT*2)
        code2.shift(RIGHT*2)

        self.play(Write(code),Write(code2))
        self.wait(6)
        self.play(FadeOut(code),FadeOut(code2),FadeOut(zm3))

        end=TextMobject("return 0;",color=YELLOW)

        end.scale(3)

        self.play(Write(end))
        
        self.play(Uncreate(end),FadeOut(title))

        self.wait(2)

        rem=TextMobject("对了，答案")

        self.play(Write(rem))

        self.wait(1)

        ans=TextMobject("$114514^{1919810}\\%1e7=295904128$\\\\运算用时小于一秒\\\\但...毫无要素（可惜了）")

        self.play(Transform(rem,ans))

        self.wait(2)

        self.play(FadeOutAndShift(rem))