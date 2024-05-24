def extract_tag(ancestor, selector=None, attribute=None, return_list=False):
    try:
        if return_list:
            return [tag.text.strip() for tag in ancestor.select(selector)]
        if not selector and attribute:
            return ancestor[attribute]
        if attribute:
            return ancestor.select_one(selector)[attribute].strip()
        return ancestor.select_one(selector).text.strip()
    except (AttributeError, TypeError):
        return None

selectors = {
    "offer_id": [None, "data-test-offerid"],
    "job": ["h2.tiles_h1yuv00i"],
    "company": ["a.core_n194fgoq > h3"],
    "location":["h4.tiles_r1h1nge7"],
    "link":["div.tiles_c1k2agp8 > a", "href"]
}
sub_selectors = {
    "responsibilities": ["section.c1x52cbk:nth-child(5) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(1) ~ .tkzmjn3", None, True],
    "requirements": ["section.c1x52cbk:nth-child(6) > div:nth-child(2) > section:nth-child(1) > div.c1vseyc8:nth-child(1) > ul:nth-child(1) > li:nth-child(1) ~ .tkzmjn3", None, True],
    "optional_requirements": ["section.s1e9dfkj:nth-child(2) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(1) ~ .tkzmjn3", None, True]
}


