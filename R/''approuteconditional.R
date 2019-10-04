# AUTO GENERATED FILE - DO NOT EDIT

''approuteconditional <- function(children=NULL, id=NULL, route=NULL, className=NULL, tag=NULL) {
    
    props <- list(children=children, id=id, route=route, className=className, tag=tag)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'approuteconditional',
        namespace = 'dcc',
        propNames = c('children', 'id', 'route', 'className', 'tag'),
        package = 'dcc'
        )

    structure(component, class = c('dash_component', 'list'))
}
