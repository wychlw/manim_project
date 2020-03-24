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
        t0=TextMobject("很简单？")
        t0.set_color(BLUE)
        t1=TextMobject("遍历+一一比较")
        t1.set_color(BLUE)

        ##position



        ##Showing object
        self.play(FadeIn(t0))
        self.wait(1)
        self.play(Transform(t0,t1))
        self.wait(1)
        

        ## Marking object
        text0_0=TextMobject("俾斯麦曾经说过，对于不屈不挠的人来说，没有失败这回事。")
        text0_1=TextMobject("这")
        text0_2=TextMobject("似乎")
        text0_3=TextMobject("解答了我的疑惑。 现在，解决哈希算法的问题，")
        text0_4=TextMobject("是非常非常重要的。 就我个人来说，哈希算法对我的意义，\\\\不能不说非常重大。")
        text0=VGroup(text0_0,text0_1,text0_2,text0_3,text0_4)
        text1_0=TextMobject("俾斯麦曾经说过，对于不屈不挠的人来说，没有失败这回事。")
        text1_1=TextMobject("这")
        text1_2=TextMobject("好似")
        text1_3=TextMobject("解答了我的疑惑。 现在，解决哈希算法的问题，")
        text1_4=TextMobject("是非常非常重要的。 就我个人来说，哈希算法对我的意义，\\\\不能不说非常重大。")
        text1=VGroup(text1_0,text1_1,text1_2,text1_3,text1_4)

        ## position
        text0_1.next_to(text0_0.get_corner(DOWN+LEFT),DOWN+RIGHT)
        text0_2.next_to(text0_1.get_right(),RIGHT)
        text0_3.next_to(text0_2.get_right(),RIGHT)
        text0_4.next_to(text0_3.get_bottom(),DOWN)
        text0.to_edge(UP)
        text1_1.next_to(text1_0.get_corner(DOWN+LEFT),DOWN+RIGHT)
        text1_2.next_to(text1_1.get_right(),RIGHT)
        text1_3.next_to(text1_2.get_right(),RIGHT)
        text1_4.next_to(text1_3.get_bottom(),DOWN)
        text1.to_edge(DOWN)

        ##Showing object
        self.play(FadeIn(text0))
        self.play(FadeIn(text1))
        self.wait(1)
        text0_2.set_color(ORANGE)
        text1_2.set_color(RED)
        self.wait(1)
        sc1=VGroup(t0,text0,text1)
        self.play(FadeOut(sc1))
