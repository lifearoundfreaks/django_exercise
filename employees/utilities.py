class PaginationSetter():
    def __init__(self, page_amount, page, max_pages=11):
        # If there's more than than max_pages pages, this should be used
        if page_amount > max_pages:
            layout = {}
            limit = (max_pages // 2) - 2
            # If there's more than max_pages AND page is at left edge
            if page <= limit + 3:
                layout.update(dict.fromkeys(
                    range(1, max_pages - 1), ""))
                layout["..."] = "disabled"
                layout[page_amount] = ""
            # If there's more than max_pages AND page is at right edge
            elif page > page_amount - limit - 2:
                layout[1] = ""
                layout["..."] = "disabled"
                layout.update(dict.fromkeys(
                    range(page_amount - max_pages + 3, page_amount + 1), ""))
            # If there's more than max_pages AND page is NOT at edge
            else:
                layout[1] = ""
                layout["..."] = "disabled"
                layout.update(dict.fromkeys(
                    range(page - limit, page + limit + max_pages % 2), ""))
                layout["... "] = "disabled"
                layout[page_amount] = ""

            layout[page] = "active"

        # If there's max_pages or less pages, this one should be used
        else:
            layout = {i: "" if i != page else "active" for i in range(
                1, page_amount + 1)}

        # Let's get the proper layout from layouts dictionary
        self.pages = layout

        # Finally, check if we need 'previous' and 'next' buttons
        self.previous = "" if page != 1 else "disabled"
        self.next = "" if page != page_amount else "disabled"
