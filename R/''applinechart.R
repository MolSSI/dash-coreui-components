# AUTO GENERATED FILE - DO NOT EDIT

''applinechart <- function(id=NULL, className=NULL, tag=NULL, style=NULL) {
    
    props <- list(id=id, className=className, tag=tag, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'applinechart',
        namespace = 'dcc',
        propNames = c('id', 'className', 'tag', 'style'),
        package = 'dcc'
        )

    structure(component, class = c('dash_component', 'list'))
}
