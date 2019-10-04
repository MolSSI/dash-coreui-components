# AUTO GENERATED FILE - DO NOT EDIT

''appcard <- function(children=NULL, id=NULL, className=NULL, tag=NULL, style=NULL) {
    
    props <- list(children=children, id=id, className=className, tag=tag, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'appcard',
        namespace = 'dcc',
        propNames = c('children', 'id', 'className', 'tag', 'style'),
        package = 'dcc'
        )

    structure(component, class = c('dash_component', 'list'))
}
