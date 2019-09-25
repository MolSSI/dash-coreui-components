# AUTO GENERATED FILE - DO NOT EDIT

''appnavbarbrand <- function(children=NULL, tag=NULL, id=NULL, className=NULL, brand=NULL, full=NULL, minimized=NULL) {
    
    props <- list(children=children, tag=tag, id=id, className=className, brand=brand, full=full, minimized=minimized)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'appnavbarbrand',
        namespace = 'dcc',
        propNames = c('children', 'tag', 'id', 'className', 'brand', 'full', 'minimized'),
        package = 'dcc'
        )

    structure(component, class = c('dash_component', 'list'))
}
