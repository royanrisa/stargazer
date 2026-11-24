# === Stage 10: Постраничный вывод ===
# Project: StarGazer
def paginate(objects, page, per_page):
    if per_page <= 0:
        per_page = 1
    if page < 1:
        page = 1
    total_pages = (len(objects) + per_page - 1) // per_page
    if page > total_pages:
        page = total_pages
    start = (page - 1) * per_page
    end = start + per_page
    return {
        "page": page,
        "per_page": per_page,
        "total_pages": total_pages,
        "total": len(objects),
        "items": objects[start:end],
        "has_next": page < total_pages,
        "has_prev": page > 1,
    }


def build_pagination_meta(page, per_page, total):
    if per_page <= 0:
        per_page = 1
    total_pages = (total + per_page - 1) // per_page
    if page < 1:
        page = 1
    if page > total_pages:
        page = total_pages
    return {
        "page": page,
        "per_page": per_page,
        "total_pages": total_pages,
        "total": total,
        "has_next": page < total_pages,
        "has_prev": page > 1,
    }


def format_page_link(page, per_page, total, label):
    if per_page <= 0:
        per_page = 1
    total_pages = (total + per_page - 1) // per_page
    if page < 1:
        page = 1
    if page > total_pages:
        page = total_pages
    return f"[{label} {page}/{total_pages}]"


def format_pages_range(page, per_page, total):
    if per_page <= 0:
        per_page = 1
    total_pages = (total + per_page - 1) // per_page
    if page < 1:
        page = 1
    if page > total_pages:
        page = total_pages
    pages = []
    for i in range(1, total_pages + 1):
        pages.append(i)
    return pages


def get_object_name(obj):
    return obj.get("name", "")


def get_object_type(obj):
    return obj.get("type", "")


def get_object_magnitude(obj):
    return obj.get("magnitude", None)


def get_object_constellation(obj):
    return obj.get("constellation", "")


def get_object_page(objects, page, per_page):
    return paginate(objects, page, per_page)
