# AUTO GENERATED FILE - DO NOT EDIT

''appheaderdropdown <- function(children=NULL, id=NULL, direction=NULL) {
    
    props <- list(children=children, id=id, direction=direction)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'appheaderdropdown',
        namespace = 'dcc',
        propNames = c('children', 'id', 'direction'),
        package = 'dcc'
        )

    structure(component, class = c('dash_component', 'list'))
}
