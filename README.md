# Atom One Dark Vivid Theme

This is the [Atom Vivid Syntax Theme](https://github.com/nschneid/vivid-syntax), recreated for VS Code.

The Atom theme was created by substituting several text colors in the [One Dark](https://github.com/atom/one-dark-syntax) theme.

Accordingly, this is a fork of the [VS Code version of the One Dark theme](https://github.com/akamud/vscode-theme-onedark) by akamud.


![](https://raw.githubusercontent.com/nschneid/vscode-theme-onedark-vivid/master/screenshots/preview.png)

## Color Substitutions

Mirroring the [Atom version](https://github.com/nschneid/vivid-syntax/compare/f481d062d5605fe85e905556ffc2d781eb6a3a66...nschneid:vivid-syntax:master#diff-4cdb52a9f32fd0060585e9d37ac98980f88d5d0c2151bfb12b374e104276c3f7), substitutions are as follows:

```less
@hue-1:   hsl(187, 47%, 55%); // <-cyan #36AABA (#56B6C2 in the new theme)
@hue-1:   hsl( 95, 38%, 62%); // <-green #98C379 (builtin, regexp escape, etc.)

@hue-2:   hsl(207, 82%, 66%); // <-blue #61AFEF
@hue-2:   hsl(207, 82%, 66%); // <-(function/method name, etc.)

@hue-3:   hsl(286, 60%, 67%); // <-purple #DEB1EC (#C678DD in the new theme)
@hue-3:   hsl(334, 100%, 70%); // <-magenta #FF66A8 (keyword, regexp backreference or start/end of string, etc.)

@hue-4:   hsl( 95, 38%, 62%); // <-green #98C379
@hue-4:   rgb(195, 161, 242); // <-purple #C3A1F2 (string, etc.)

@hue-5:   hsl(355, 65%, 65%); // <-red 1 #E06C75
@hue-5:   hsl(334, 100%, 70%); // <-magenta #FF66A8 (non-Python variable, tag, etc.)

@hue-5-2: hsl(  5, 48%, 51%); // <-red 2 #BE5046
@hue-5-2: hsl(  5, 48%, 51%); //

@hue-6:   hsl( 29, 54%, 61%); // <-orange 1 #D19A66
@hue-6:   hsl(30, 100%, 70%); // <-orange 1 #FFB366 (attribute, numeric/constant, special value, string placeholder, regexp character class, etc.)

@hue-6-2: hsl( 39, 67%, 69%); // <-orange 2 #E5C07B
@hue-6-2: hsl(30, 100%, 70%); // <-orange 2 #FFB366 (class name)
```

## Customization

If you are using VSCode 1.12+ versions you can customize the colors to your liking, overriding the ones provided by this theme. More info [here](https://code.visualstudio.com/docs/getstarted/theme-color-reference).

### Custom Font

The original One Dark theme does not use a custom font, for that reason I don't supply a custom font either, but  you might be used to see screenshots of the One Dark theme using the [Fira Mono](https://github.com/mozilla/Fira) font. You can easily [customize your settings](https://code.visualstudio.com/docs/getstarted/settings) to use it.  
If you download and install the font in your system, you can add this option to have a custom font:

```json
{
    "editor.fontFamily": "YOUR FONT, Menlo, Monaco, 'Courier New', monospace"
}
```
