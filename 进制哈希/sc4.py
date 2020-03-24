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

        fi=TextMobject("File",color="#87CEEB")
        rec=Rectangle()
        File=VGroup(fi,rec)

        arr=Arrow()
        ys=TextMobject("映射")
        poi=VGroup(arr,ys)

        to=TextMobject("\"str\"")

        app=VGroup(File,poi,to)

        rec.surround(fi)
        ys.next_to(arr.get_top(),UP)

        File.next_to(poi.get_left(),LEFT)
        to.next_to(poi.get_right(),RIGHT)

        app.to_edge(UP)

        ell=Ellipse(color=BLUE)
        ell.surround(app)
        rule=TextMobject("规则")
        hx=TextMobject("哈希算法",color="#B0C4DE")
        hx.scale(1.5)
        arr2=Arrow(ell,hx)
        rule.next_to(arr2.get_right(),RIGHT)
        ru=VGroup(arr2,rule)

        self.play(FadeInFrom(app,DOWN))
        self.wait(1)
        self.play(FadeIn(ell))
        self.play(FadeIn(ru))
        self.play(FadeIn(hx))
        self.wait(1)
        self.play(FadeOut(app),FadeOut(ell),FadeOut(ru))
        self.play(ApplyMethod(hx.to_edge,UP))
        self.wait(1)

        define=TextMobject("将一个不定长输入转换成一个定长输出")
        define.next_to(hx.get_bottom(),DOWN+DOWN)
        self.play(Write(define))
        self.wait(1)
        self.play(FadeOut(define))

        eg=TextMobject("eg:")
        eg.scale(1.2)
        m0=TextMobject("*0")
        m0.scale(1.2)
        n=TextMobject("N")
        n.scale(1.2)

        eg.next_to(m0.get_left(),LEFT)
        n.next_to(m0.get_left(),LEFT)

        equ=TextMobject("=0")
        equ.scale(1.2)
        equ.next_to(m0.get_right(),RIGHT)

        self.play(FadeIn(eg),FadeIn(m0))
        self.wait(1)
        self.play(Transform(eg,n),FadeIn(equ))
        self.wait(1)

        fh=TextMobject("完美符合定义")
        ng=TextMobject("但...没啥用")

        fh.next_to(m0.get_bottom(),DOWN)
        ng.next_to(fh.get_bottom(),DOWN)

        self.play(FadeIn(fh))
        self.play(FadeIn(ng))
        self.wait(1)
        self.play(FadeOut(eg),FadeOut(m0),FadeOut(equ))
        self.play(FadeOut(fh),FadeOut(ng))
        self.wait(1)

        need=TextMobject("抗强碰撞性")
        need.next_to(hx.get_bottom(),DOWN*4)

        self.play(FadeIn(need))
        self.wait(1)

        hxe=TextMobject("HASH")
        obj1=TextMobject("Object1")
        obj1.to_edge(LEFT)
        obj1.shift(UP*2)
        obj2=TextMobject("Object2")
        obj2.to_edge(LEFT)
        obj2.shift(DOWN*2)
        o1th=Arrow(obj1,hxe)
        o2th=Arrow(obj2,hxe)
        o1=VGroup(obj1,o1th)
        o2=VGroup(obj2,o2th)

        obj1o=TextMobject("Out1")
        obj1o.to_edge(RIGHT)
        obj1o.shift(UP*2)
        obj2o=TextMobject("Out2")
        obj2o.to_edge(RIGHT)
        obj2o.shift(DOWN*2)
        hto1=Arrow(hxe,obj1o)
        hto2=Arrow(hxe,obj2o)
        o1o=VGroup(hto1,obj1o)
        o2o=VGroup(hto2,obj2o)

        ne=TextMobject("$\\neq$")
        ne.to_edge(RIGHT)
        ne.shift(LEFT*0.5)
        ne.rotate(TAU/4)
        ne.scale(2)

        self.play(FadeIn(hxe))
        self.play(FadeIn(o1),FadeIn(o2))
        self.play(FadeIn(o1o),FadeIn(o2o))
        self.play(FadeIn(ne))
        self.wait(1)
        self.play(FadeOut(hx),FadeOut(hxe),FadeOut(o1),FadeOut(o2),FadeOut(o1o),FadeOut(o2o),FadeOut(ne),FadeOut(need))
        self.wait(1)