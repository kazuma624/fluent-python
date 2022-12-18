def tag(name, *content, cls=None, **attrs):
    """Generate one or more HTML tags"""
    if cls:
        # class は Python の予約後なので直接使わないようにしている
        attrs['class'] = cls

    if attrs:
        attr_str = ''.join(
            f' {attr}="{value}"'for attr, value in sorted(attrs.items())
        )
    else:
        attr_str = ''

    if content:
        return '\n'.join(
            f'<{name}{attr_str}>{c}</{name}{attr_str}>' for c in content
        )
    else:
        return f'<{name}{attr_str} />'

