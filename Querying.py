def select_links(inverted_index, Query):

    Query = Query.split(' ')

    links = set()

    for i in Query:
        if i in inverted_index.keys():
            links.update(inverted_index[i])

    return links
