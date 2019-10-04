% Auto-generated: do not edit by hand
\name{''appsidebarnav}

\alias{''appsidebarnav}

\title{appsidebarnav component}

\description{
CoreUI sidebar nav component.  This component manages the location in a multi-page much as Dash Core Components `Location` component. It is also compatible with the Dash Core Components `Link` component. See https://dash.plot.ly/urls for details.
}

\usage{
''appsidebarnav(children=NULL, id=NULL, className=NULL, pathname=NULL, search=NULL, hash=NULL,
href=NULL, refresh=NULL, navConfig=NULL, navFunc=NULL, isOpen=NULL,
staticContext=NULL, tag=NULL)
}

\arguments{
\item{children}{A list of or a singular dash component, string or number. The children, defaults to `navConfig.items`.}

\item{id}{Character. The ID used to identify this component in Dash callbacks, defaults to `appsidebarnav`.}

\item{className}{Character. The CSS class name, defaults to `sidebar-nav`.}

\item{pathname}{Character. The pathname in window.location - e.g., "/my/full/pathname"}

\item{search}{Character. The search in window.location - e.g., "?myargument=1"}

\item{hash}{Character. The hash in window.location - e.g., "#myhash"}

\item{href}{Character. The href in window.location - e.g., "/my/full/pathname?myargument=1#myhash"}

\item{refresh}{Logical. Refresh the page when the location is updated? Default to `true`.}

\item{navConfig}{Logical | numeric | character | named list | unnamed list. The sidebar nav config, used to configure the contents of this sidebar nav.
Alternatively, you can add children manually, which will cause this prop to be ignored.
A sidebar nav config object has the following structure:
- title:
````js
{
  title: true,
  name: 'Theme',
  class: ''              // optional class names space delimited list for title item ex: "text-center"
  wrapper: {             // optional wrapper object
    element: '',         // optional* valid HTML5 element tag ( *required when passing attributes)
    attributes: {}       // optional valid JS object with JS API naming ex: { className: "my-class", style: { fontFamily: "Verdana" }, id: "my-id"}
  },
},
````
- item:
````js
{
  name: 'Dashboard',
  url: '/dashboard',
  icon: `icon-speedometer',
  class: '',                    // optional
  variant: 'success',           // optional
  badge: {
    variant: 'info',
    text: 'NEW',
    class: ''                   // optional
  },
  attributes: { target: '_blank', rel: "noreferrer noopener", disabled: false, hidden: false }, // (v2.1.0 up) optional valid JS object with JS API naming
},
````
- item with `children` array - works like `nav-dropdown-toggle` with `nav-dropdown-items`
````js
{
  name: 'Icons',
  url: '/icons',
  icon: 'icon-star',
  children: [
    {
      name: 'Flags',     // item options apply
      url: '/icons/flags',
      icon: 'icon-star',
      badge: {
        variant: 'success',
        text: 'NEW'
      }
    },
  ]
}
````
- divider:
````js
{
  divider: true
},
````

- order of precedence:
````
title > divider > children > item
````}

\item{navFunc}{Character. TODO document this.}

\item{isOpen}{Logical. The isOpen flag, defaults to `false`.}

\item{staticContext}{Logical | numeric | character | named list | unnamed list. TODO document this.}

\item{tag}{Character. The HTML tag, defaults to `nav`.}
}
