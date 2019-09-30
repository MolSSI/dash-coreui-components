# AUTO GENERATED FILE - DO NOT EDIT

''appasidetoggler <- function(children=NULL, id=NULL, className=NULL, defaultOpen=NULL, display=NULL, mobile=NULL, tag=NULL, type=NULL) {
    
    props <- list(children=children, id=id, className=className, defaultOpen=defaultOpen, display=display, mobile=mobile, tag=tag, type=type)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'appasidetoggler',
        namespace = 'dcc',
        propNames = c('children', 'id', 'className', 'defaultOpen', 'display', 'mobile', 'tag', 'type'),
        package = 'dcc'
        )

    structure(component, class = c('dash_component', 'list'))
}
