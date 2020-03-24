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

class my_scene(Scene):

    def construct(self):
        
        ## Marking object

        title=TextMobject("映射", color=BLUE)
        rec=Rectangle(color=GRAY)
        gou=VGroup(title,rec)

        ## Position

        rec.surround(title)

        ## Showing object

        self.play(Write(title))
        self.wait(0.5)
        self.play(FadeIn(rec))
        self.wait(0.5)
        self.play(ApplyMethod(gou.scale,2.5))
        self.wait(0.5)
        self.play(FadeOutAndShiftDown(gou,direction=DOWN))

        ## Marking object

        ell0=Ellipse(color=BLUE)
        txt0=TextMobject("一个东西",color=GRAY)
        gou1=VGroup(ell0,txt0)
        arr0=Arrow(color=BLUE)
        txt1=TextMobject("指代（对应）",color=GRAY)
        gou2=VGroup(arr0,txt1)
        ell1=Ellipse(color=BLUE)
        txt2=TextMobject("另一个东西",color=GRAY)
        gou3=VGroup(ell1,txt2)
        gou_all=VGroup(gou1,gou2,gou3)
        txt3=TextMobject("苹果")
        txt3.set_color("#4169E1")
        txt4=TextMobject("1")
        txt4.set_color("#4169E1")

        ell0_0=Ellipse(color=BLUE)
        txt0_0=TextMobject("鸡蛋",color="#4169E1")
        gou1_0=VGroup(ell0_0,txt0_0)
        arr0_0=Arrow(color=BLUE)
        txt1_0=TextMobject("指代（对应）",color=GRAY)
        gou2_0=VGroup(arr0_0,txt1_0)
        ell1_0=Ellipse(color=BLUE)
        txt2_0=TextMobject("2",color="#4169E1")
        gou3_0=VGroup(ell1_0,txt2_0)
        gou_all0=VGroup(gou1_0,gou2_0,gou3_0)

        ## Position

        ell0.surround(txt0)
        ell1.surround(txt2)
        txt1.next_to(arr0.get_top(),UP)
        gou1.next_to(gou2.get_left(),LEFT)
        gou3.next_to(gou2.get_right(),RIGHT)
        gou_all.to_edge(edge=UP)
        txt3.next_to(txt0.get_left())
        txt4.next_to(txt2.get_center()+LEFT*0.2)

        ell0_0.surround(txt0_0)
        ell0_0.scale(2)
        ell1_0.surround(txt2_0)
        ell1_0.scale(4)
        txt1_0.next_to(arr0_0.get_top(),UP)
        gou1_0.next_to(gou2_0.get_left(),LEFT)
        gou3_0.next_to(gou2_0.get_right(),RIGHT)
        gou_all0.to_edge(edge=DOWN)

        ## Showing object

        self.wait(5)
        self.play(FadeInFrom(gou_all, UP))
        self.wait(1)
        self.play(Transform(txt0,txt3),Transform(txt2,txt4),FadeInFrom(gou_all0, DOWN))
        self.wait(1)
        self.play(FadeOut(gou_all),FadeOut(gou_all0))
