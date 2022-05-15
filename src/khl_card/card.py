import json
from typing import Optional, List, Union, Tuple

from .color import Color
from .modules import _Module
from .types import ThemeTypes, SizeTypes, NamedColor

__all__ = ['Card']


class Card:
    """
    构建卡片
    """
    type: str = 'card'
    theme: str
    size: str
    color: Optional[str]
    modules: List[_Module]

    def __init__(self, *modules: _Module, theme: Union[str, ThemeTypes] = ThemeTypes.PRIMARY,
                 size: Union[str, SizeTypes] = SizeTypes.LG, color: Union[Color, NamedColor, str, None] = None) -> None:
        """
        构建卡片

        :param modules: 卡片模块列表
        :param theme: 卡片主题
        :param size: 目前只支持sm与lg。 lg仅在PC端有效, 在移动端不管填什么，均为sm。
        :param color: 卡片颜色 ex: #55ffff or NamedColor.XXX
        """
        self.modules = list(modules)
        self.theme = theme
        self.size = size
        if color is None:
            self.color = None
        elif isinstance(color, str):
            self.color = color
        elif isinstance(color, Color):
            self.color = color.__str__()
        elif isinstance(color, NamedColor):
            self.color = color.value.__str__()
        else:
            raise ValueError('incorrect color value: ' + self.color)

    def __getitem__(self, item: int):
        return self.modules[item]

    def build(self) -> dict:
        """
        :return: 构造后卡片
        """
        ret = {'type': self.type, 'theme': self.theme, 'size': self.size, 'modules': []}
        if self.color is not None:
            ret['color'] = self.color
        for i in self.modules:
            ret['modules'].append(i.build())
        return ret

    def build_to_json(self) -> str:
        return json.dumps(self.build(), indent=4, ensure_ascii=False)

    def append(self, module: _Module):
        self.modules.append(module)

    def clear(self):
        self.modules.clear()

    def set_theme(self, theme: Union[str, ThemeTypes]):
        self.theme = theme if isinstance(theme, str) else theme.value

    def set_size(self, size: Union[str, SizeTypes]):
        self.size = size if isinstance(size, str) else size.value

    def set_color(self, color: Union[str, Color, NamedColor, None]):
        if color is None:
            self.color = None
        elif isinstance(color, str):
            self.color = color
        elif isinstance(color, Color):
            self.color = color.__str__()
        elif isinstance(color, NamedColor):
            self.color = color.value.__str__()
        else:
            raise ValueError('incorrect color value: ' + self.color)
