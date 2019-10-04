# AUTO GENERATED FILE - DO NOT EDIT

''appbreadcrumb <- function(children=NULL, id=NULL, className=NULL, appRoutes=NULL, tag=NULL) {
    
    props <- list(children=children, id=id, className=className, appRoutes=appRoutes, tag=tag)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'appbreadcrumb',
        namespace = 'dcc',
        propNames = c('children', 'id', 'className', 'appRoutes', 'tag'),
        package = 'dcc'
        )

    structure(component, class = c('dash_component', 'list'))
}
