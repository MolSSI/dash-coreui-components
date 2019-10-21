# AUTO GENERATED FILE - DO NOT EDIT

''apptableheader <- function(children=NULL, id=NULL, className=NULL, tag=NULL, style=NULL, data=NULL) {
    
    props <- list(children=children, id=id, className=className, tag=tag, style=style, data=data)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'apptableheader',
        namespace = 'dcc',
        propNames = c('children', 'id', 'className', 'tag', 'style', 'data'),
        package = 'dcc'
        )

    structure(component, class = c('dash_component', 'list'))
}
