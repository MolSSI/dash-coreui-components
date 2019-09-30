# AUTO GENERATED FILE - DO NOT EDIT

''appsidebar <- function(children=NULL, id=NULL, className=NULL, compact=NULL, display=NULL, fixed=NULL, minimized=NULL, isOpen=NULL, offCanvas=NULL, staticContext=NULL, tag=NULL) {
    
    props <- list(children=children, id=id, className=className, compact=compact, display=display, fixed=fixed, minimized=minimized, isOpen=isOpen, offCanvas=offCanvas, staticContext=staticContext, tag=tag)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'appsidebar',
        namespace = 'dcc',
        propNames = c('children', 'id', 'className', 'compact', 'display', 'fixed', 'minimized', 'isOpen', 'offCanvas', 'staticContext', 'tag'),
        package = 'dcc'
        )

    structure(component, class = c('dash_component', 'list'))
}
