# AUTO GENERATED FILE - DO NOT EDIT

''appsidebarnav <- function(children=NULL, id=NULL, className=NULL, pathname=NULL, search=NULL, hash=NULL, href=NULL, refresh=NULL, navConfig=NULL, navFunc=NULL, isOpen=NULL, staticContext=NULL, tag=NULL) {
    
    props <- list(children=children, id=id, className=className, pathname=pathname, search=search, hash=hash, href=href, refresh=refresh, navConfig=navConfig, navFunc=navFunc, isOpen=isOpen, staticContext=staticContext, tag=tag)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'appsidebarnav',
        namespace = 'dcc',
        propNames = c('children', 'id', 'className', 'pathname', 'search', 'hash', 'href', 'refresh', 'navConfig', 'navFunc', 'isOpen', 'staticContext', 'tag'),
        package = 'dcc'
        )

    structure(component, class = c('dash_component', 'list'))
}
