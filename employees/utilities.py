class PaginationSetter():
    def __init__(self, page_amount, page):
        # This dictionary stores different layouts for paginator
        layouts = {
            # If there's 5 or less pages, this one should be used
            5: {i: "" if i != page else "active" for i in range(
                1, page_amount + 1)},
            # If there's more than than 5 pages, this should be used
            6: {
                1: "",
                "...": "disabled",
                page: "active",
                "... ": "disabled",
                page_amount: "",
            },
            # If there's more than 5 AND page is 1, 2, n-1 or n (at edge)
            7: {
                1: "" if page != 1 else "active",
                2: "" if page != 2 else "active",
                "...": "disabled",
                page_amount - 1: "" if page != page_amount - 1 else "active",
                page_amount: "" if page != page_amount else "active",
            },
        }
        # Is page at the edge of list? (1, 2, n-1 or n)
        if page_amount > 5:
            page_at_edge = page < 3 or page > page_amount - 2
        else:
            page_at_edge = False

        # Let's get the proper layout from layouts dictionary
        self.pages = layouts[min(max(page_amount, 5), 6) + page_at_edge]

        # Finally, check if we need 'previous' and 'next' buttons
        self.previous = "" if page != 1 else "disabled"
        self.next = "" if page != page_amount else "disabled"
