





<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
  <link rel="dns-prefetch" href="https://assets-cdn.github.com">
  <link rel="dns-prefetch" href="https://avatars0.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars1.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars2.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars3.githubusercontent.com">
  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com">
  <link rel="dns-prefetch" href="https://user-images.githubusercontent.com/">



  <link crossorigin="anonymous" media="all" integrity="sha512-pCRDtdb3GlUU48h+oRJVA8f0GddrLnU97wB7mHQ7q6c40vMbMMZsFdk0IMhkUFRqw1M/y4EkWxtaKwfeFezOkQ==" rel="stylesheet" href="https://assets-cdn.github.com/assets/frameworks-73f533b7cc08a9d040e601cfd38fa585.css" />
  <link crossorigin="anonymous" media="all" integrity="sha512-pscKt6TONS3P9zPqdDjngC5prTq2tL4UT8MfWSiqhftwRK8aipsxEuebGlIpobamrDHDV//uvSMkcPXLduUrWw==" rel="stylesheet" href="https://assets-cdn.github.com/assets/github-a0a727fb61e0eacfb1f33d2f365272f8.css" />
  
  
  
  

  <meta name="viewport" content="width=device-width">
  
  <title>cpython/argparse.rst at master · python/cpython</title>
    <meta name="description" content="GitHub is where people build software. More than 28 million people use GitHub to discover, fork, and contribute to over 85 million projects.">
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
  <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
  <meta property="fb:app_id" content="1401488693436528">

    
    <meta property="og:image" content="https://avatars2.githubusercontent.com/u/1525981?s=400&amp;v=4" /><meta property="og:site_name" content="GitHub" /><meta property="og:type" content="object" /><meta property="og:title" content="python/cpython" /><meta property="og:url" content="https://github.com/python/cpython" /><meta property="og:description" content="cpython - The Python programming language" />

  <link rel="assets" href="https://assets-cdn.github.com/">
  <link rel="web-socket" href="wss://live.github.com/_sockets/VjI6MjcxMTE5NjUxOmFlOWFiZTYwOWM3NzZmMzE4NTVmOWNhMWNhNWQ0ZjBlMTc5NDYyYmFlMjk0MjhlOTU0YjQxNWMyZWQ3M2NjNzY=--796e2ce87c3acb42a1def8014d6600427d11a7c7">
  <meta name="pjax-timeout" content="1000">
  <link rel="sudo-modal" href="/sessions/sudo_modal">
  <meta name="request-id" content="D394:162D:79E8:ED5C:5B36ACFE" data-pjax-transient>


  

  <meta name="selected-link" value="repo_source" data-pjax-transient>

    <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
  <meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">
  <meta name="google-site-verification" content="GXs5KoUUkNCoaAZn7wPN-t01Pywp9M3sEjnt_3_ZWPc">
    <meta name="google-analytics" content="UA-3769691-2">

<meta name="octolytics-host" content="collector.githubapp.com" /><meta name="octolytics-app-id" content="github" /><meta name="octolytics-event-url" content="https://collector.githubapp.com/github-external/browser_event" /><meta name="octolytics-dimension-request_id" content="D394:162D:79E8:ED5C:5B36ACFE" /><meta name="octolytics-dimension-region_edge" content="iad" /><meta name="octolytics-dimension-region_render" content="iad" /><meta name="octolytics-actor-id" content="16306768" /><meta name="octolytics-actor-login" content="LeonCloudEndure" /><meta name="octolytics-actor-hash" content="71edd88dda6999435a41f2f11a5bb64acf5e6f9af1be0113ee30f1eba404c810" />
<meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-pjax-transient="true" />




<meta class="js-ga-set" name="dimension1" content="Logged In">


  

      <meta name="hostname" content="github.com">
    <meta name="user-login" content="LeonCloudEndure">

      <meta name="expected-hostname" content="github.com">
    <meta name="js-proxy-site-detection-payload" content="ZGY3N2FjZGNkY2MxODQ2YTJkZmViYWZlMjA3MTM5NmI2NmYwNGQ5ZDJlZjcxMmYyYzA0NTZkNzQ2N2VmYjNlN3x7InJlbW90ZV9hZGRyZXNzIjoiNzcuMTYxLjE0Ny4xODEiLCJyZXF1ZXN0X2lkIjoiRDM5NDoxNjJEOjc5RTg6RUQ1Qzo1QjM2QUNGRSIsInRpbWVzdGFtcCI6MTUzMDMwOTg4NiwiaG9zdCI6ImdpdGh1Yi5jb20ifQ==">

    <meta name="enabled-features" content="UNIVERSE_BANNER,FREE_TRIALS,MARKETPLACE_INSIGHTS,MARKETPLACE_SEARCH,MARKETPLACE_INSIGHTS_CONVERSION_PERCENTAGES">

  <meta name="html-safe-nonce" content="1ad9b4f17554671cc24de5ecfa0b3323a6686099">

  <meta http-equiv="x-pjax-version" content="28e6687e0aef26fe64025c1be61f33a7">
  

      <link href="https://github.com/python/cpython/commits/master.atom" rel="alternate" title="Recent Commits to cpython:master" type="application/atom+xml">

  <meta name="description" content="cpython - The Python programming language">
  <meta name="go-import" content="github.com/python/cpython git https://github.com/python/cpython.git">

  <meta name="octolytics-dimension-user_id" content="1525981" /><meta name="octolytics-dimension-user_login" content="python" /><meta name="octolytics-dimension-repository_id" content="81598961" /><meta name="octolytics-dimension-repository_nwo" content="python/cpython" /><meta name="octolytics-dimension-repository_public" content="true" /><meta name="octolytics-dimension-repository_is_fork" content="false" /><meta name="octolytics-dimension-repository_network_root_id" content="81598961" /><meta name="octolytics-dimension-repository_network_root_nwo" content="python/cpython" /><meta name="octolytics-dimension-repository_explore_github_marketplace_ci_cta_shown" content="false" />


    <link rel="canonical" href="https://github.com/python/cpython/blob/master/Doc/library/argparse.rst" data-pjax-transient>


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <link rel="mask-icon" href="https://assets-cdn.github.com/pinned-octocat.svg" color="#000000">
  <link rel="icon" type="image/x-icon" class="js-site-favicon" href="https://assets-cdn.github.com/favicon.ico">

<meta name="theme-color" content="#1e2327">



<link rel="manifest" href="/manifest.json" crossOrigin="use-credentials">

  </head>

  <body class="logged-in env-production page-blob">
    

  <div class="position-relative js-header-wrapper ">
    <a href="#start-of-content" tabindex="1" class="p-3 bg-blue text-white show-on-focus js-skip-to-content">Skip to content</a>
    <div id="js-pjax-loader-bar" class="pjax-loader-bar"><div class="progress"></div></div>

    
    
    



        
<header class="Header  f5" role="banner">
  <div class="d-flex flex-justify-between px-3 container-lg">
    <div class="d-flex flex-justify-between ">
      <div class="">
        <a class="header-logo-invertocat" href="https://github.com/" data-hotkey="g d" aria-label="Homepage" data-ga-click="Header, go to dashboard, icon:logo">
  <svg height="32" class="octicon octicon-mark-github" viewBox="0 0 16 16" version="1.1" width="32" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
</a>

      </div>

    </div>

    <div class="HeaderMenu d-flex flex-justify-between flex-auto">
      <div class="d-flex">
            <div class="">
              <div class="header-search scoped-search site-scoped-search js-site-search position-relative js-jump-to"
  role="search combobox"
  aria-owns="jump-to-results"
  aria-label="Search or jump to"
  aria-haspopup="listbox"
  aria-expanded="true"
>
  <div class="position-relative">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-site-search-form" data-scope-type="Repository" data-scope-id="81598961" data-scoped-search-url="/python/cpython/search" data-unscoped-search-url="/search" action="/python/cpython/search" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
      <label class="form-control header-search-wrapper header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container">
        <input type="text"
          class="form-control header-search-input jump-to-field js-jump-to-field js-site-search-focus js-site-search-field is-clearable"
          data-hotkey="s,/"
          name="q"
          value=""
          placeholder="Search or jump to…"
          data-unscoped-placeholder="Search or jump to…"
          data-scoped-placeholder="Search or jump to…"
          autocapitalize="off"
          aria-autocomplete="list"
          aria-controls="jump-to-results"
          data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations#csrf-token=x5TaVIGVmblDQ25ELvp7XeLF/apUaqFgpW2qcUZYOlBlomx9+qhD7w3fywGH5pcrga3LYOW2hVIgOZJmg53h4g=="
          spellcheck="false"
          autocomplete="off"
          >
          <input type="hidden" class="js-site-search-type-field" name="type" >
            <img src="https://assets-cdn.github.com/images/search-shortcut-hint.svg" alt="" class="mr-2 header-search-key-slash">

            <div class="Box position-absolute overflow-hidden d-none jump-to-suggestions js-jump-to-suggestions-container">
              <ul class="d-none js-jump-to-suggestions-template-container">
                <li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item">
                  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center p-2 jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open" href="">
                    <div class="jump-to-octicon js-jump-to-octicon mr-2 text-center d-none"></div>
                    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar" alt="" aria-label="Team" src="" width="28" height="28">

                    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden no-wrap css-truncate css-truncate-target">
                    </div>

                    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
                      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
                        In this repository
                      </span>
                      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
                        All GitHub
                      </span>
                      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
                    </div>

                    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
                      Jump to
                      <span class="d-inline-block ml-1 v-align-middle">↵</span>
                    </div>
                  </a>
                </li>
                <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-repo-octicon-template" title="Repository" aria-label="Repository" viewBox="0 0 12 16" version="1.1" role="img"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
                <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-project-octicon-template" title="Project" aria-label="Project" viewBox="0 0 15 16" version="1.1" role="img"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"/></svg>
                <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-search-octicon-template" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M15.7 13.3l-3.81-3.83A5.93 5.93 0 0 0 13 6c0-3.31-2.69-6-6-6S1 2.69 1 6s2.69 6 6 6c1.3 0 2.48-.41 3.47-1.11l3.83 3.81c.19.2.45.3.7.3.25 0 .52-.09.7-.3a.996.996 0 0 0 0-1.41v.01zM7 10.7c-2.59 0-4.7-2.11-4.7-4.7 0-2.59 2.11-4.7 4.7-4.7 2.59 0 4.7 2.11 4.7 4.7 0 2.59-2.11 4.7-4.7 4.7z"/></svg>
              </ul>
              <ul class="d-none js-jump-to-no-results-template-container">
                <li class="d-flex flex-justify-center flex-items-center p-3 f5 d-none">
                  <span class="text-gray">No suggested jump to results</span>
                </li>
              </ul>

              <ul id="jump-to-results" class="js-navigation-container jump-to-suggestions-results-container js-jump-to-suggestions-results-container" >
                <li class="d-flex flex-justify-center flex-items-center p-0 f5">
                  <img src="https://assets-cdn.github.com/images/spinners/octocat-spinner-128.gif" alt="Octocat Spinner Icon" class="m-2" width="28">
                </li>
              </ul>
            </div>
      </label>
</form>  </div>
</div>

            </div>

          <ul class="d-flex pl-2 flex-items-center text-bold list-style-none" role="navigation">
            <li>
              <a class="js-selected-navigation-item HeaderNavlink px-2" data-hotkey="g p" data-ga-click="Header, click, Nav menu - item:pulls context:user" aria-label="Pull requests you created" data-selected-links="/pulls /pulls/assigned /pulls/mentioned /pulls" href="/pulls">
                Pull requests
</a>            </li>
            <li>
              <a class="js-selected-navigation-item HeaderNavlink px-2" data-hotkey="g i" data-ga-click="Header, click, Nav menu - item:issues context:user" aria-label="Issues you created" data-selected-links="/issues /issues/assigned /issues/mentioned /issues" href="/issues">
                Issues
</a>            </li>
              <li>
                <a class="js-selected-navigation-item HeaderNavlink px-2" data-ga-click="Header, click, Nav menu - item:marketplace context:user" data-octo-click="marketplace_click" data-octo-dimensions="location:nav_bar" data-selected-links=" /marketplace" href="/marketplace">
                   Marketplace
</a>              </li>
            <li>
              <a class="js-selected-navigation-item HeaderNavlink px-2" data-ga-click="Header, click, Nav menu - item:explore" data-selected-links="/explore /trending /trending/developers /integrations /integrations/feature/code /integrations/feature/collaborate /integrations/feature/ship showcases showcases_search showcases_landing /explore" href="/explore">
                Explore
</a>            </li>
          </ul>
      </div>

      <div class="d-flex">
        
<ul class="user-nav d-flex flex-items-center list-style-none" id="user-links">
  <li class="dropdown">
    <span class="d-inline-block  px-2">
      
    <a aria-label="You have no unread notifications" class="notification-indicator tooltipped tooltipped-s  js-socket-channel js-notification-indicator" data-hotkey="g n" data-ga-click="Header, go to notifications, icon:read" data-channel="notification-changed:16306768" href="/notifications">
        <span class="mail-status "></span>
        <svg class="octicon octicon-bell" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M13.99 11.991v1H0v-1l.73-.58c.769-.769.809-2.547 1.189-4.416.77-3.767 4.077-4.996 4.077-4.996 0-.55.45-1 .999-1 .55 0 1 .45 1 1 0 0 3.387 1.229 4.156 4.996.38 1.879.42 3.657 1.19 4.417l.659.58h-.01zM6.995 15.99c1.11 0 1.999-.89 1.999-1.999H4.996c0 1.11.89 1.999 1.999 1.999z"/></svg>
</a>
    </span>
  </li>

  <li class="dropdown">
    <details class="details-overlay details-reset js-dropdown-details d-flex px-2 flex-items-center">
      <summary class="HeaderNavlink"
         aria-label="Create new…"
         data-ga-click="Header, create new, icon:add">
        <svg class="octicon octicon-plus float-left mr-1 mt-1" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 9H7v5H5V9H0V7h5V2h2v5h5v2z"/></svg>
        <span class="dropdown-caret mt-1"></span>
      </summary>

      <ul class="dropdown-menu dropdown-menu-sw">
        
<a class="dropdown-item" href="/new" data-ga-click="Header, create new repository">
  New repository
</a>

  <a class="dropdown-item" href="/new/import" data-ga-click="Header, import a repository">
    Import repository
  </a>

<a class="dropdown-item" href="https://gist.github.com/" data-ga-click="Header, create new gist">
  New gist
</a>

  <a class="dropdown-item" href="/organizations/new" data-ga-click="Header, create new organization">
    New organization
  </a>




      </ul>
    </details>
  </li>

  <li class="dropdown">

    <details class="details-overlay details-reset js-dropdown-details d-flex pl-2 flex-items-center">
      <summary class="HeaderNavlink name mt-1"
        aria-label="View profile and more"
        data-ga-click="Header, show menu, icon:avatar">
        <img alt="@LeonCloudEndure" class="avatar float-left mr-1" src="https://avatars2.githubusercontent.com/u/16306768?s=40&amp;v=4" height="20" width="20">
        <span class="dropdown-caret"></span>
      </summary>

      <ul class="dropdown-menu dropdown-menu-sw">
        <li class="dropdown-header header-nav-current-user css-truncate">
          Signed in as <strong class="css-truncate-target">LeonCloudEndure</strong>
        </li>

        <li class="dropdown-divider"></li>

        <li><a class="dropdown-item" href="/LeonCloudEndure" data-ga-click="Header, go to profile, text:your profile">
          Your profile
        </a></li>
        <li><a class="dropdown-item" href="/LeonCloudEndure?tab=stars" data-ga-click="Header, go to starred repos, text:your stars">
          Your stars
        </a></li>
          <li><a class="dropdown-item" href="https://gist.github.com/" data-ga-click="Header, your gists, text:your gists">Your gists</a></li>

        <li class="dropdown-divider"></li>

        <li><a class="dropdown-item" href="https://help.github.com" data-ga-click="Header, go to help, text:help">
          Help
        </a></li>

        <li><a class="dropdown-item" href="/settings/profile" data-ga-click="Header, go to settings, icon:settings">
          Settings
        </a></li>

        <li><!-- '"` --><!-- </textarea></xmp> --></option></form><form class="logout-form" action="/logout" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="979rFZ4pc/3MEzZEeQsEvWMBHa6hUrzICVn5MJ3PdCWQzkVg5m6JEnFlzPLlOlGQnwun6lIwwg3o43h1F05Otg==" />
          <button type="submit" class="dropdown-item dropdown-signout" data-ga-click="Header, sign out, icon:logout">
            Sign out
          </button>
        </form></li>
      </ul>
    </details>
  </li>
</ul>



        <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="sr-only right-0" action="/logout" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="4ObBmlGKzV/aYcVQpQoKfWZ3TBI8vMpo/X41kQFPy8SHl+/vKc03sGcXP+Y5O19Qmn32Vs/etK0cxLTUi87xVw==" />
          <button type="submit" class="dropdown-item dropdown-signout" data-ga-click="Header, sign out, icon:logout">
            Sign out
          </button>
</form>      </div>
    </div>
  </div>
</header>

      

  </div>

  <div id="start-of-content" class="show-on-focus"></div>

    <div id="js-flash-container">
</div>



  <div role="main" class="application-main ">
        <div itemscope itemtype="http://schema.org/SoftwareSourceCode" class="">
    <div id="js-repo-pjax-container" data-pjax-container >
      





  



  <div class="pagehead repohead instapaper_ignore readability-menu experiment-repo-nav  ">
    <div class="repohead-details-container clearfix container">

      <ul class="pagehead-actions">
  <li>
        <!-- '"` --><!-- </textarea></xmp> --></option></form><form data-autosubmit="true" data-remote="true" class="js-social-container" action="/notifications/subscribe" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="rAbbQAh+8meksMaKU95bZWiWzcyDU/smTKUdVXqO8j30b4oaKCD3CUeTemwrfa8oRseN8aRIBaFKAs7IZhEtLA==" />      <input type="hidden" name="repository_id" id="repository_id" value="81598961" class="form-control" />

        <div class="select-menu js-menu-container js-select-menu">
          <a href="/python/cpython/subscription"
            class="btn btn-sm btn-with-count select-menu-button js-menu-target"
            role="button"
            aria-haspopup="true"
            aria-expanded="false"
            aria-label="Toggle repository notifications menu"
            data-ga-click="Repository, click Watch settings, action:blob#show">
            <span class="js-select-button">
                <svg class="octicon octicon-eye" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
                Watch
            </span>
          </a>
          <a class="social-count js-social-count"
            href="/python/cpython/watchers"
            aria-label="892 users are watching this repository">
            892
          </a>

        <div class="select-menu-modal-holder">
          <div class="select-menu-modal subscription-menu-modal js-menu-content">
            <div class="select-menu-header js-navigation-enable" tabindex="-1">
              <svg class="octicon octicon-x js-menu-close" role="img" aria-label="Close" viewBox="0 0 12 16" version="1.1" width="12" height="16"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
              <span class="select-menu-title">Notifications</span>
            </div>

              <div class="select-menu-list js-navigation-container" role="menu">

                <div class="select-menu-item js-navigation-item selected" role="menuitem" tabindex="0">
                  <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
                  <div class="select-menu-item-text">
                    <input type="radio" name="do" id="do_included" value="included" checked="checked" />
                    <span class="select-menu-item-heading">Not watching</span>
                    <span class="description">Be notified when participating or @mentioned.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <svg class="octicon octicon-eye" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
                      Watch
                    </span>
                  </div>
                </div>

                <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                  <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
                  <div class="select-menu-item-text">
                    <input type="radio" name="do" id="do_subscribed" value="subscribed" />
                    <span class="select-menu-item-heading">Watching</span>
                    <span class="description">Be notified of all conversations.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <svg class="octicon octicon-eye" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
                        Unwatch
                    </span>
                  </div>
                </div>

                <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                  <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
                  <div class="select-menu-item-text">
                    <input type="radio" name="do" id="do_ignore" value="ignore" />
                    <span class="select-menu-item-heading">Ignoring</span>
                    <span class="description">Never be notified.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <svg class="octicon octicon-mute" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 2.81v10.38c0 .67-.81 1-1.28.53L3 10H1c-.55 0-1-.45-1-1V7c0-.55.45-1 1-1h2l3.72-3.72C7.19 1.81 8 2.14 8 2.81zm7.53 3.22l-1.06-1.06-1.97 1.97-1.97-1.97-1.06 1.06L11.44 8 9.47 9.97l1.06 1.06 1.97-1.97 1.97 1.97 1.06-1.06L13.56 8l1.97-1.97z"/></svg>
                        Stop ignoring
                    </span>
                  </div>
                </div>

              </div>

            </div>
          </div>
        </div>
</form>
  </li>

  <li>
    
  <div class="js-toggler-container js-social-container starring-container ">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="starred js-social-form" action="/python/cpython/unstar" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="kl0OcFpQp2oEUX+8asWpoZELSCXbLIzam4Db8tLTlRS1FmMV/3XoKYsaesO5mPgCQfLsedO+07tsaJrYnL+vjQ==" />
      <input type="hidden" name="context" value="repository"></input>
      <button
        type="submit"
        class="btn btn-sm btn-with-count js-toggler-target"
        aria-label="Unstar this repository" title="Unstar python/cpython"
        data-ga-click="Repository, click unstar button, action:blob#show; text:Unstar">
        <svg class="octicon octicon-star" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74L14 6z"/></svg>
        Unstar
      </button>
        <a class="social-count js-social-count" href="/python/cpython/stargazers"
           aria-label="18389 users starred this repository">
          18,389
        </a>
</form>
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="unstarred js-social-form" action="/python/cpython/star" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="OOhAU4Kj2FoIT76RBdT0lAbWdN75QdlRklBV1zoHjrtVONnD9MUZAbjT/rv2M3zPzi+Q4ptbrSMhqZf4jTDU7Q==" />
      <input type="hidden" name="context" value="repository"></input>
      <button
        type="submit"
        class="btn btn-sm btn-with-count js-toggler-target"
        aria-label="Star this repository" title="Star python/cpython"
        data-ga-click="Repository, click star button, action:blob#show; text:Star">
        <svg class="octicon octicon-star" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74L14 6z"/></svg>
        Star
      </button>
        <a class="social-count js-social-count" href="/python/cpython/stargazers"
           aria-label="18389 users starred this repository">
          18,389
        </a>
</form>  </div>

  </li>

  <li>
          <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="btn-with-count" action="/python/cpython/fork" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="W3i2j2PeNOreNIWgaz3FjCaUSapPnw2APLui3Tl4nAy2w3i497Bk9jMMdcREXnu1rhoIO4c9qxh4u+ee74QdIQ==" />
            <button
                type="submit"
                class="btn btn-sm btn-with-count"
                data-ga-click="Repository, show fork modal, action:blob#show; text:Fork"
                title="Fork your own copy of python/cpython to your account"
                aria-label="Fork your own copy of python/cpython to your account">
              <svg class="octicon octicon-repo-forked" viewBox="0 0 10 16" version="1.1" width="10" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 1a1.993 1.993 0 0 0-1 3.72V6L5 8 3 6V4.72A1.993 1.993 0 0 0 2 1a1.993 1.993 0 0 0-1 3.72V6.5l3 3v1.78A1.993 1.993 0 0 0 5 15a1.993 1.993 0 0 0 1-3.72V9.5l3-3V4.72A1.993 1.993 0 0 0 8 1zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3 10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3-10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
              Fork
            </button>
</form>
    <a href="/python/cpython/network" class="social-count"
       aria-label="5844 users forked this repository">
      5,844
    </a>
  </li>
</ul>

      <h1 class="public ">
  <svg class="octicon octicon-repo" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
  <span class="author" itemprop="author"><a class="url fn" rel="author" href="/python">python</a></span><!--
--><span class="path-divider">/</span><!--
--><strong itemprop="name"><a data-pjax="#js-repo-pjax-container" href="/python/cpython">cpython</a></strong>

</h1>

    </div>
    
<nav class="reponav js-repo-nav js-sidenav-container-pjax container"
     itemscope
     itemtype="http://schema.org/BreadcrumbList"
     role="navigation"
     data-pjax="#js-repo-pjax-container">

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a class="js-selected-navigation-item selected reponav-item" itemprop="url" data-hotkey="g c" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages /python/cpython" href="/python/cpython">
      <svg class="octicon octicon-code" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M9.5 3L8 4.5 11.5 8 8 11.5 9.5 13 14 8 9.5 3zm-5 0L0 8l4.5 5L6 11.5 2.5 8 6 4.5 4.5 3z"/></svg>
      <span itemprop="name">Code</span>
      <meta itemprop="position" content="1">
</a>  </span>


  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a data-hotkey="g p" itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_pulls checks /python/cpython/pulls" href="/python/cpython/pulls">
      <svg class="octicon octicon-git-pull-request" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
      <span itemprop="name">Pull requests</span>
      <span class="Counter">765</span>
      <meta itemprop="position" content="3">
</a>  </span>




  <a class="js-selected-navigation-item reponav-item" data-selected-links="repo_graphs repo_contributors dependency_graph pulse /python/cpython/pulse" href="/python/cpython/pulse">
    <svg class="octicon octicon-graph" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M16 14v1H0V0h1v14h15zM5 13H3V8h2v5zm4 0H7V3h2v10zm4 0h-2V6h2v7z"/></svg>
    Insights
</a>

</nav>


  </div>

<div class="container new-discussion-timeline experiment-repo-nav  ">
  <div class="repository-content ">

    
  <a class="d-none js-permalink-shortcut" data-hotkey="y" href="/python/cpython/blob/b57eea16d19d2cd7244eae370cb3cf68f922e2f9/Doc/library/argparse.rst">Permalink</a>

  <!-- blob contrib key: blob_contributors:v21:600a239f01380067f3529038b3ad4f11 -->

  

  <div class="file-navigation">
    
<div class="select-menu branch-select-menu js-menu-container js-select-menu float-left">
  <button class=" btn btn-sm select-menu-button js-menu-target css-truncate" data-hotkey="w"
    
    type="button" aria-label="Switch branches or tags" aria-expanded="false" aria-haspopup="true">
      <i>Branch:</i>
      <span class="js-select-button css-truncate-target">master</span>
  </button>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax>

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <svg class="octicon octicon-x js-menu-close" role="img" aria-label="Close" viewBox="0 0 12 16" version="1.1" width="12" height="16"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
        <span class="select-menu-title">Switch branches/tags</span>
      </div>

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="form-control js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" data-filter-placeholder="Filter branches/tags" class="js-select-menu-tab" role="tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" data-filter-placeholder="Find a tag…" class="js-select-menu-tab" role="tab">Tags</a>
            </li>
          </ul>
        </div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches" role="menu">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/python/cpython/blob/2.7/Doc/library/argparse.rst"
               data-name="2.7"
               data-skip-pjax="true"
               rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2.7
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/python/cpython/blob/3.4/Doc/library/argparse.rst"
               data-name="3.4"
               data-skip-pjax="true"
               rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3.4
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/python/cpython/blob/3.5/Doc/library/argparse.rst"
               data-name="3.5"
               data-skip-pjax="true"
               rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3.5
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/python/cpython/blob/3.6/Doc/library/argparse.rst"
               data-name="3.6"
               data-skip-pjax="true"
               rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3.6
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/python/cpython/blob/3.7/Doc/library/argparse.rst"
               data-name="3.7"
               data-skip-pjax="true"
               rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3.7
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open selected"
               href="/python/cpython/blob/master/Doc/library/argparse.rst"
               data-name="master"
               data-skip-pjax="true"
               rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                master
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/python/cpython/blob/ncoghlan-bpo-33499-whats-new/Doc/library/argparse.rst"
               data-name="ncoghlan-bpo-33499-whats-new"
               data-skip-pjax="true"
               rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                ncoghlan-bpo-33499-whats-new
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/python/cpython/blob/revert-7960-backport-2cc9d21-3.7/Doc/library/argparse.rst"
               data-name="revert-7960-backport-2cc9d21-3.7"
               data-skip-pjax="true"
               rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                revert-7960-backport-2cc9d21-3.7
              </span>
            </a>
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.7.0/Doc/library/argparse.rst"
              data-name="v3.7.0"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.7.0">
                v3.7.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.7.0rc1/Doc/library/argparse.rst"
              data-name="v3.7.0rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.7.0rc1">
                v3.7.0rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.7.0b5/Doc/library/argparse.rst"
              data-name="v3.7.0b5"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.7.0b5">
                v3.7.0b5
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.7.0b4/Doc/library/argparse.rst"
              data-name="v3.7.0b4"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.7.0b4">
                v3.7.0b4
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.7.0b3/Doc/library/argparse.rst"
              data-name="v3.7.0b3"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.7.0b3">
                v3.7.0b3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.7.0b2/Doc/library/argparse.rst"
              data-name="v3.7.0b2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.7.0b2">
                v3.7.0b2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.7.0b1/Doc/library/argparse.rst"
              data-name="v3.7.0b1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.7.0b1">
                v3.7.0b1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.7.0a4/Doc/library/argparse.rst"
              data-name="v3.7.0a4"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.7.0a4">
                v3.7.0a4
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.7.0a3/Doc/library/argparse.rst"
              data-name="v3.7.0a3"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.7.0a3">
                v3.7.0a3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.7.0a2/Doc/library/argparse.rst"
              data-name="v3.7.0a2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.7.0a2">
                v3.7.0a2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.7.0a1/Doc/library/argparse.rst"
              data-name="v3.7.0a1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.7.0a1">
                v3.7.0a1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.6.6/Doc/library/argparse.rst"
              data-name="v3.6.6"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.6.6">
                v3.6.6
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.6.6rc1/Doc/library/argparse.rst"
              data-name="v3.6.6rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.6.6rc1">
                v3.6.6rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.6.5/Doc/library/argparse.rst"
              data-name="v3.6.5"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.6.5">
                v3.6.5
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.6.5rc1/Doc/library/argparse.rst"
              data-name="v3.6.5rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.6.5rc1">
                v3.6.5rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.6.4/Doc/library/argparse.rst"
              data-name="v3.6.4"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.6.4">
                v3.6.4
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.6.4rc1/Doc/library/argparse.rst"
              data-name="v3.6.4rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.6.4rc1">
                v3.6.4rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.6.3/Doc/library/argparse.rst"
              data-name="v3.6.3"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.6.3">
                v3.6.3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.6.3rc1/Doc/library/argparse.rst"
              data-name="v3.6.3rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.6.3rc1">
                v3.6.3rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.6.2/Doc/library/argparse.rst"
              data-name="v3.6.2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.6.2">
                v3.6.2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.6.2rc2/Doc/library/argparse.rst"
              data-name="v3.6.2rc2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.6.2rc2">
                v3.6.2rc2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.6.2rc1/Doc/library/argparse.rst"
              data-name="v3.6.2rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.6.2rc1">
                v3.6.2rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.6.1/Doc/library/argparse.rst"
              data-name="v3.6.1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.6.1">
                v3.6.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.6.1rc1/Doc/library/argparse.rst"
              data-name="v3.6.1rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.6.1rc1">
                v3.6.1rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.6.0/Doc/library/argparse.rst"
              data-name="v3.6.0"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.6.0">
                v3.6.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.6.0rc2/Doc/library/argparse.rst"
              data-name="v3.6.0rc2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.6.0rc2">
                v3.6.0rc2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.6.0rc1/Doc/library/argparse.rst"
              data-name="v3.6.0rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.6.0rc1">
                v3.6.0rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.6.0b4/Doc/library/argparse.rst"
              data-name="v3.6.0b4"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.6.0b4">
                v3.6.0b4
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.6.0b3/Doc/library/argparse.rst"
              data-name="v3.6.0b3"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.6.0b3">
                v3.6.0b3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.6.0b2/Doc/library/argparse.rst"
              data-name="v3.6.0b2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.6.0b2">
                v3.6.0b2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.6.0b1/Doc/library/argparse.rst"
              data-name="v3.6.0b1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.6.0b1">
                v3.6.0b1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.6.0a4/Doc/library/argparse.rst"
              data-name="v3.6.0a4"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.6.0a4">
                v3.6.0a4
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.6.0a3/Doc/library/argparse.rst"
              data-name="v3.6.0a3"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.6.0a3">
                v3.6.0a3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.6.0a2/Doc/library/argparse.rst"
              data-name="v3.6.0a2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.6.0a2">
                v3.6.0a2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.6.0a1/Doc/library/argparse.rst"
              data-name="v3.6.0a1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.6.0a1">
                v3.6.0a1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.5.5/Doc/library/argparse.rst"
              data-name="v3.5.5"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.5.5">
                v3.5.5
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.5.5rc1/Doc/library/argparse.rst"
              data-name="v3.5.5rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.5.5rc1">
                v3.5.5rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.5.4/Doc/library/argparse.rst"
              data-name="v3.5.4"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.5.4">
                v3.5.4
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.5.4rc1/Doc/library/argparse.rst"
              data-name="v3.5.4rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.5.4rc1">
                v3.5.4rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.5.3/Doc/library/argparse.rst"
              data-name="v3.5.3"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.5.3">
                v3.5.3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.5.3rc1/Doc/library/argparse.rst"
              data-name="v3.5.3rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.5.3rc1">
                v3.5.3rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.5.2/Doc/library/argparse.rst"
              data-name="v3.5.2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.5.2">
                v3.5.2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.5.2rc1/Doc/library/argparse.rst"
              data-name="v3.5.2rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.5.2rc1">
                v3.5.2rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.5.1/Doc/library/argparse.rst"
              data-name="v3.5.1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.5.1">
                v3.5.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.5.1rc1/Doc/library/argparse.rst"
              data-name="v3.5.1rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.5.1rc1">
                v3.5.1rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.5.0/Doc/library/argparse.rst"
              data-name="v3.5.0"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.5.0">
                v3.5.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.5.0rc4/Doc/library/argparse.rst"
              data-name="v3.5.0rc4"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.5.0rc4">
                v3.5.0rc4
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.5.0rc3/Doc/library/argparse.rst"
              data-name="v3.5.0rc3"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.5.0rc3">
                v3.5.0rc3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.5.0rc2/Doc/library/argparse.rst"
              data-name="v3.5.0rc2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.5.0rc2">
                v3.5.0rc2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.5.0rc1/Doc/library/argparse.rst"
              data-name="v3.5.0rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.5.0rc1">
                v3.5.0rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.5.0b4/Doc/library/argparse.rst"
              data-name="v3.5.0b4"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.5.0b4">
                v3.5.0b4
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.5.0b3/Doc/library/argparse.rst"
              data-name="v3.5.0b3"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.5.0b3">
                v3.5.0b3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.5.0b2/Doc/library/argparse.rst"
              data-name="v3.5.0b2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.5.0b2">
                v3.5.0b2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.5.0b1/Doc/library/argparse.rst"
              data-name="v3.5.0b1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.5.0b1">
                v3.5.0b1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.5.0a4/Doc/library/argparse.rst"
              data-name="v3.5.0a4"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.5.0a4">
                v3.5.0a4
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.5.0a3/Doc/library/argparse.rst"
              data-name="v3.5.0a3"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.5.0a3">
                v3.5.0a3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.5.0a2/Doc/library/argparse.rst"
              data-name="v3.5.0a2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.5.0a2">
                v3.5.0a2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.5.0a1/Doc/library/argparse.rst"
              data-name="v3.5.0a1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.5.0a1">
                v3.5.0a1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.4.8/Doc/library/argparse.rst"
              data-name="v3.4.8"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.4.8">
                v3.4.8
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.4.8rc1/Doc/library/argparse.rst"
              data-name="v3.4.8rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.4.8rc1">
                v3.4.8rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.4.7/Doc/library/argparse.rst"
              data-name="v3.4.7"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.4.7">
                v3.4.7
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.4.7rc1/Doc/library/argparse.rst"
              data-name="v3.4.7rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.4.7rc1">
                v3.4.7rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.4.6/Doc/library/argparse.rst"
              data-name="v3.4.6"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.4.6">
                v3.4.6
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.4.6rc1/Doc/library/argparse.rst"
              data-name="v3.4.6rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.4.6rc1">
                v3.4.6rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.4.5/Doc/library/argparse.rst"
              data-name="v3.4.5"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.4.5">
                v3.4.5
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.4.5rc1/Doc/library/argparse.rst"
              data-name="v3.4.5rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.4.5rc1">
                v3.4.5rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.4.4/Doc/library/argparse.rst"
              data-name="v3.4.4"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.4.4">
                v3.4.4
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.4.4rc1/Doc/library/argparse.rst"
              data-name="v3.4.4rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.4.4rc1">
                v3.4.4rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.4.3/Doc/library/argparse.rst"
              data-name="v3.4.3"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.4.3">
                v3.4.3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.4.3rc1/Doc/library/argparse.rst"
              data-name="v3.4.3rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.4.3rc1">
                v3.4.3rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.4.2/Doc/library/argparse.rst"
              data-name="v3.4.2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.4.2">
                v3.4.2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.4.2rc1/Doc/library/argparse.rst"
              data-name="v3.4.2rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.4.2rc1">
                v3.4.2rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.4.1/Doc/library/argparse.rst"
              data-name="v3.4.1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.4.1">
                v3.4.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.4.1rc1/Doc/library/argparse.rst"
              data-name="v3.4.1rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.4.1rc1">
                v3.4.1rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.4.0/Doc/library/argparse.rst"
              data-name="v3.4.0"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.4.0">
                v3.4.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.4.0rc3/Doc/library/argparse.rst"
              data-name="v3.4.0rc3"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.4.0rc3">
                v3.4.0rc3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.4.0rc2/Doc/library/argparse.rst"
              data-name="v3.4.0rc2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.4.0rc2">
                v3.4.0rc2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.4.0rc1/Doc/library/argparse.rst"
              data-name="v3.4.0rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.4.0rc1">
                v3.4.0rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.4.0b3/Doc/library/argparse.rst"
              data-name="v3.4.0b3"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.4.0b3">
                v3.4.0b3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.4.0b2/Doc/library/argparse.rst"
              data-name="v3.4.0b2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.4.0b2">
                v3.4.0b2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.4.0b1/Doc/library/argparse.rst"
              data-name="v3.4.0b1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.4.0b1">
                v3.4.0b1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.4.0a4/Doc/library/argparse.rst"
              data-name="v3.4.0a4"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.4.0a4">
                v3.4.0a4
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.4.0a3/Doc/library/argparse.rst"
              data-name="v3.4.0a3"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.4.0a3">
                v3.4.0a3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.4.0a2/Doc/library/argparse.rst"
              data-name="v3.4.0a2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.4.0a2">
                v3.4.0a2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.4.0a1/Doc/library/argparse.rst"
              data-name="v3.4.0a1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.4.0a1">
                v3.4.0a1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.3.7/Doc/library/argparse.rst"
              data-name="v3.3.7"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.3.7">
                v3.3.7
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.3.7rc1/Doc/library/argparse.rst"
              data-name="v3.3.7rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.3.7rc1">
                v3.3.7rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.3.6/Doc/library/argparse.rst"
              data-name="v3.3.6"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.3.6">
                v3.3.6
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.3.6rc1/Doc/library/argparse.rst"
              data-name="v3.3.6rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.3.6rc1">
                v3.3.6rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.3.5/Doc/library/argparse.rst"
              data-name="v3.3.5"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.3.5">
                v3.3.5
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.3.5rc2/Doc/library/argparse.rst"
              data-name="v3.3.5rc2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.3.5rc2">
                v3.3.5rc2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.3.5rc1/Doc/library/argparse.rst"
              data-name="v3.3.5rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.3.5rc1">
                v3.3.5rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.3.4/Doc/library/argparse.rst"
              data-name="v3.3.4"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.3.4">
                v3.3.4
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.3.4rc1/Doc/library/argparse.rst"
              data-name="v3.3.4rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.3.4rc1">
                v3.3.4rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.3.3/Doc/library/argparse.rst"
              data-name="v3.3.3"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.3.3">
                v3.3.3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.3.3rc2/Doc/library/argparse.rst"
              data-name="v3.3.3rc2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.3.3rc2">
                v3.3.3rc2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.3.3rc1/Doc/library/argparse.rst"
              data-name="v3.3.3rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.3.3rc1">
                v3.3.3rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.3.2/Doc/library/argparse.rst"
              data-name="v3.3.2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.3.2">
                v3.3.2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.3.1/Doc/library/argparse.rst"
              data-name="v3.3.1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.3.1">
                v3.3.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/python/cpython/tree/v3.3.1rc1/Doc/library/argparse.rst"
              data-name="v3.3.1rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.3.1rc1">
                v3.3.1rc1
              </span>
            </a>
        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div>

    </div>
  </div>
</div>

    <div class="BtnGroup float-right">
      <a href="/python/cpython/find/master"
            class="js-pjax-capture-input btn btn-sm BtnGroup-item"
            data-pjax
            data-hotkey="t">
        Find file
      </a>
      <clipboard-copy for="blob-path" class="btn btn-sm BtnGroup-item">
        Copy path
      </clipboard-copy>
    </div>
    <div id="blob-path" class="breadcrumb">
      <span class="repo-root js-repo-root"><span class="js-path-segment"><a data-pjax="true" href="/python/cpython"><span>cpython</span></a></span></span><span class="separator">/</span><span class="js-path-segment"><a data-pjax="true" href="/python/cpython/tree/master/Doc"><span>Doc</span></a></span><span class="separator">/</span><span class="js-path-segment"><a data-pjax="true" href="/python/cpython/tree/master/Doc/library"><span>library</span></a></span><span class="separator">/</span><strong class="final-path">argparse.rst</strong>
    </div>
  </div>


  
  <div class="commit-tease">
      <span class="float-right">
        <a class="commit-tease-sha" href="/python/cpython/commit/8ebf5ceb0f5408d1ebc26c19702ac0762ef5ea04" data-pjax>
          8ebf5ce
        </a>
        <relative-time datetime="2018-05-24T01:55:15Z">May 24, 2018</relative-time>
      </span>
      <div>
        <a rel="contributor" data-skip-pjax="true" data-hovercard-user-id="5833005" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/ned-deily"><img class="avatar" src="https://avatars0.githubusercontent.com/u/5833005?s=40&amp;v=4" width="20" height="20" alt="@ned-deily" /></a>
        <a class="user-mention" rel="contributor" data-hovercard-user-id="5833005" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/ned-deily">ned-deily</a>
          <a data-pjax="true" title="bpo-33109: argparse subparsers are once again not required by default (GH-6919)

bpo-26510 in 3.7.0a2 changed the behavior of argparse to make
subparsers required by default, returning to the behavior of 2.7
and 3.2. The behavior was changed in 3.3 to be no longer required.
While it might make more sense to have the default to required,
compatibility with 3.3 through 3.6 is probably less disruptive
than trying to reintroduce compatibility with 2.7 at this point.
This change restores the 3.6 behavior." class="message" href="/python/cpython/commit/8ebf5ceb0f5408d1ebc26c19702ac0762ef5ea04">bpo-33109: argparse subparsers are once again not required by default (</a><a class="issue-link js-issue-link" data-error-text="Failed to load issue title" data-id="323762440" data-permission-text="Issue title is private" data-url="https://github.com/python/cpython/issues/6919" href="https://github.com/python/cpython/pull/6919">…</a>
      </div>

    <div class="commit-tease-contributors">
      <button type="button" class="btn-link muted-link contributors-toggle" data-facebox="#blob_contributors_box">
        <strong>28</strong>
         contributors
      </button>
          <a class="avatar-link" data-hovercard-user-id="25624924" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/python/cpython/commits/master/Doc/library/argparse.rst?author=ezio-melotti">
      <img class="avatar" src="https://avatars3.githubusercontent.com/u/25624924?s=40&amp;v=4" width="20" height="20" alt="@ezio-melotti" /> 
</a>    <a class="avatar-link" data-hovercard-user-id="144359" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/python/cpython/commits/master/Doc/library/argparse.rst?author=birkenfeld">
      <img class="avatar" src="https://avatars2.githubusercontent.com/u/144359?s=40&amp;v=4" width="20" height="20" alt="@birkenfeld" /> 
</a>    <a class="avatar-link" data-hovercard-user-id="346648" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/python/cpython/commits/master/Doc/library/argparse.rst?author=sandrotosi">
      <img class="avatar" src="https://avatars2.githubusercontent.com/u/346648?s=40&amp;v=4" width="20" height="20" alt="@sandrotosi" /> 
</a>    <a class="avatar-link" data-hovercard-user-id="635179" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/python/cpython/commits/master/Doc/library/argparse.rst?author=merwok">
      <img class="avatar" src="https://avatars3.githubusercontent.com/u/635179?s=40&amp;v=4" width="20" height="20" alt="@merwok" /> 
</a>    <a class="avatar-link" data-hovercard-user-id="26338" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/python/cpython/commits/master/Doc/library/argparse.rst?author=berkerpeksag">
      <img class="avatar" src="https://avatars0.githubusercontent.com/u/26338?s=40&amp;v=4" width="20" height="20" alt="@berkerpeksag" /> 
</a>    <a class="avatar-link" data-hovercard-user-id="1024659" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/python/cpython/commits/master/Doc/library/argparse.rst?author=vadmium">
      <img class="avatar" src="https://avatars2.githubusercontent.com/u/1024659?s=40&amp;v=4" width="20" height="20" alt="@vadmium" /> 
</a>    <a class="avatar-link" data-hovercard-user-id="1118599" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/python/cpython/commits/master/Doc/library/argparse.rst?author=bethard">
      <img class="avatar" src="https://avatars1.githubusercontent.com/u/1118599?s=40&amp;v=4" width="20" height="20" alt="@bethard" /> 
</a>    <a class="avatar-link" data-hovercard-user-id="476443" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/python/cpython/commits/master/Doc/library/argparse.rst?author=bitdancer">
      <img class="avatar" src="https://avatars3.githubusercontent.com/u/476443?s=40&amp;v=4" width="20" height="20" alt="@bitdancer" /> 
</a>    <a class="avatar-link" data-hovercard-user-id="308610" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/python/cpython/commits/master/Doc/library/argparse.rst?author=jaraco">
      <img class="avatar" src="https://avatars3.githubusercontent.com/u/308610?s=40&amp;v=4" width="20" height="20" alt="@jaraco" /> 
</a>    <a class="avatar-link" data-hovercard-user-id="356399" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/python/cpython/commits/master/Doc/library/argparse.rst?author=asvetlov">
      <img class="avatar" src="https://avatars1.githubusercontent.com/u/356399?s=40&amp;v=4" width="20" height="20" alt="@asvetlov" /> 
</a>    <a class="avatar-link" data-hovercard-user-id="332330" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/python/cpython/commits/master/Doc/library/argparse.rst?author=orsenthil">
      <img class="avatar" src="https://avatars3.githubusercontent.com/u/332330?s=40&amp;v=4" width="20" height="20" alt="@orsenthil" /> 
</a>    <a class="avatar-link" data-hovercard-user-id="1623689" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/python/cpython/commits/master/Doc/library/argparse.rst?author=rhettinger">
      <img class="avatar" src="https://avatars3.githubusercontent.com/u/1623689?s=40&amp;v=4" width="20" height="20" alt="@rhettinger" /> 
</a>    <a class="avatar-link" data-hovercard-user-id="1130906" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/python/cpython/commits/master/Doc/library/argparse.rst?author=eliben">
      <img class="avatar" src="https://avatars0.githubusercontent.com/u/1130906?s=40&amp;v=4" width="20" height="20" alt="@eliben" /> 
</a>    <a class="avatar-link" data-hovercard-user-id="219470" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/python/cpython/commits/master/Doc/library/argparse.rst?author=benjaminp">
      <img class="avatar" src="https://avatars0.githubusercontent.com/u/219470?s=40&amp;v=4" width="20" height="20" alt="@benjaminp" /> 
</a>    <a class="avatar-link" data-hovercard-user-id="19036496" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/python/cpython/commits/master/Doc/library/argparse.rst?author=terryjreedy">
      <img class="avatar" src="https://avatars3.githubusercontent.com/u/19036496?s=40&amp;v=4" width="20" height="20" alt="@terryjreedy" /> 
</a>    <a class="avatar-link" data-hovercard-user-id="355822" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/python/cpython/commits/master/Doc/library/argparse.rst?author=cjerdonek">
      <img class="avatar" src="https://avatars2.githubusercontent.com/u/355822?s=40&amp;v=4" width="20" height="20" alt="@cjerdonek" /> 
</a>    <a class="avatar-link" data-hovercard-user-id="3659035" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/python/cpython/commits/master/Doc/library/argparse.rst?author=serhiy-storchaka">
      <img class="avatar" src="https://avatars0.githubusercontent.com/u/3659035?s=40&amp;v=4" width="20" height="20" alt="@serhiy-storchaka" /> 
</a>    <a class="avatar-link" data-hovercard-user-id="142113" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/python/cpython/commits/master/Doc/library/argparse.rst?author=florentx">
      <img class="avatar" src="https://avatars3.githubusercontent.com/u/142113?s=40&amp;v=4" width="20" height="20" alt="@florentx" /> 
</a>    <a class="avatar-link" data-hovercard-user-id="588792" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/python/cpython/commits/master/Doc/library/argparse.rst?author=freddrake">
      <img class="avatar" src="https://avatars0.githubusercontent.com/u/588792?s=40&amp;v=4" width="20" height="20" alt="@freddrake" /> 
</a>    <a class="avatar-link" data-hovercard-user-id="210184" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/python/cpython/commits/master/Doc/library/argparse.rst?author=warsaw">
      <img class="avatar" src="https://avatars0.githubusercontent.com/u/210184?s=40&amp;v=4" width="20" height="20" alt="@warsaw" /> 
</a>    <a class="avatar-link" data-hovercard-user-id="70927" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/python/cpython/commits/master/Doc/library/argparse.rst?author=akheron">
      <img class="avatar" src="https://avatars0.githubusercontent.com/u/70927?s=40&amp;v=4" width="20" height="20" alt="@akheron" /> 
</a>    <a class="avatar-link" data-hovercard-user-id="3646926" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/python/cpython/commits/master/Doc/library/argparse.rst?author=elenaoat">
      <img class="avatar" src="https://avatars1.githubusercontent.com/u/3646926?s=40&amp;v=4" width="20" height="20" alt="@elenaoat" /> 
</a>    <a class="avatar-link" data-hovercard-user-id="148100" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/python/cpython/commits/master/Doc/library/argparse.rst?author=invalid-email-address">
      <img class="avatar" src="https://avatars2.githubusercontent.com/u/148100?s=40&amp;v=4" width="20" height="20" alt="@invalid-email-address" /> 
</a>    <a class="avatar-link" data-hovercard-user-id="5833005" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/python/cpython/commits/master/Doc/library/argparse.rst?author=ned-deily">
      <img class="avatar" src="https://avatars0.githubusercontent.com/u/5833005?s=40&amp;v=4" width="20" height="20" alt="@ned-deily" /> 
</a>    <a class="avatar-link" data-hovercard-user-id="11985251" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/python/cpython/commits/master/Doc/library/argparse.rst?author=suic86">
      <img class="avatar" src="https://avatars2.githubusercontent.com/u/11985251?s=40&amp;v=4" width="20" height="20" alt="@suic86" /> 
</a>    <a class="avatar-link" data-hovercard-user-id="239510" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/python/cpython/commits/master/Doc/library/argparse.rst?author=JulienPalard">
      <img class="avatar" src="https://avatars1.githubusercontent.com/u/239510?s=40&amp;v=4" width="20" height="20" alt="@JulienPalard" /> 
</a>
    <button type="button" data-facebox="#blob_contributors_box" class="btn-link others-text">and others</button>

    </div>

    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header" data-facebox-id="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list" data-facebox-id="facebox-description">
          <li class="facebox-user-list-item">
            <a class="d-inline-block" data-hovercard-user-id="25624924" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/ezio-melotti"><img src="https://avatars2.githubusercontent.com/u/25624924?s=48&amp;v=4" width="24" height="24" alt="@ezio-melotti" /></a>
            <a data-hovercard-user-id="25624924" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/ezio-melotti">ezio-melotti</a>
          </li>
          <li class="facebox-user-list-item">
            <a class="d-inline-block" data-hovercard-user-id="144359" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/birkenfeld"><img src="https://avatars3.githubusercontent.com/u/144359?s=48&amp;v=4" width="24" height="24" alt="@birkenfeld" /></a>
            <a data-hovercard-user-id="144359" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/birkenfeld">birkenfeld</a>
          </li>
          <li class="facebox-user-list-item">
            <a class="d-inline-block" data-hovercard-user-id="346648" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/sandrotosi"><img src="https://avatars3.githubusercontent.com/u/346648?s=48&amp;v=4" width="24" height="24" alt="@sandrotosi" /></a>
            <a data-hovercard-user-id="346648" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/sandrotosi">sandrotosi</a>
          </li>
          <li class="facebox-user-list-item">
            <a class="d-inline-block" data-hovercard-user-id="635179" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/merwok"><img src="https://avatars2.githubusercontent.com/u/635179?s=48&amp;v=4" width="24" height="24" alt="@merwok" /></a>
            <a data-hovercard-user-id="635179" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/merwok">merwok</a>
          </li>
          <li class="facebox-user-list-item">
            <a class="d-inline-block" data-hovercard-user-id="26338" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/berkerpeksag"><img src="https://avatars1.githubusercontent.com/u/26338?s=48&amp;v=4" width="24" height="24" alt="@berkerpeksag" /></a>
            <a data-hovercard-user-id="26338" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/berkerpeksag">berkerpeksag</a>
          </li>
          <li class="facebox-user-list-item">
            <a class="d-inline-block" data-hovercard-user-id="1024659" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/vadmium"><img src="https://avatars3.githubusercontent.com/u/1024659?s=48&amp;v=4" width="24" height="24" alt="@vadmium" /></a>
            <a data-hovercard-user-id="1024659" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/vadmium">vadmium</a>
          </li>
          <li class="facebox-user-list-item">
            <a class="d-inline-block" data-hovercard-user-id="1118599" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/bethard"><img src="https://avatars0.githubusercontent.com/u/1118599?s=48&amp;v=4" width="24" height="24" alt="@bethard" /></a>
            <a data-hovercard-user-id="1118599" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/bethard">bethard</a>
          </li>
          <li class="facebox-user-list-item">
            <a class="d-inline-block" data-hovercard-user-id="476443" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/bitdancer"><img src="https://avatars2.githubusercontent.com/u/476443?s=48&amp;v=4" width="24" height="24" alt="@bitdancer" /></a>
            <a data-hovercard-user-id="476443" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/bitdancer">bitdancer</a>
          </li>
          <li class="facebox-user-list-item">
            <a class="d-inline-block" data-hovercard-user-id="308610" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/jaraco"><img src="https://avatars2.githubusercontent.com/u/308610?s=48&amp;v=4" width="24" height="24" alt="@jaraco" /></a>
            <a data-hovercard-user-id="308610" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/jaraco">jaraco</a>
          </li>
          <li class="facebox-user-list-item">
            <a class="d-inline-block" data-hovercard-user-id="356399" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/asvetlov"><img src="https://avatars0.githubusercontent.com/u/356399?s=48&amp;v=4" width="24" height="24" alt="@asvetlov" /></a>
            <a data-hovercard-user-id="356399" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/asvetlov">asvetlov</a>
          </li>
          <li class="facebox-user-list-item">
            <a class="d-inline-block" data-hovercard-user-id="332330" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/orsenthil"><img src="https://avatars2.githubusercontent.com/u/332330?s=48&amp;v=4" width="24" height="24" alt="@orsenthil" /></a>
            <a data-hovercard-user-id="332330" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/orsenthil">orsenthil</a>
          </li>
          <li class="facebox-user-list-item">
            <a class="d-inline-block" data-hovercard-user-id="1623689" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/rhettinger"><img src="https://avatars2.githubusercontent.com/u/1623689?s=48&amp;v=4" width="24" height="24" alt="@rhettinger" /></a>
            <a data-hovercard-user-id="1623689" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/rhettinger">rhettinger</a>
          </li>
          <li class="facebox-user-list-item">
            <a class="d-inline-block" data-hovercard-user-id="1130906" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/eliben"><img src="https://avatars1.githubusercontent.com/u/1130906?s=48&amp;v=4" width="24" height="24" alt="@eliben" /></a>
            <a data-hovercard-user-id="1130906" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/eliben">eliben</a>
          </li>
          <li class="facebox-user-list-item">
            <a class="d-inline-block" data-hovercard-user-id="219470" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/benjaminp"><img src="https://avatars1.githubusercontent.com/u/219470?s=48&amp;v=4" width="24" height="24" alt="@benjaminp" /></a>
            <a data-hovercard-user-id="219470" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/benjaminp">benjaminp</a>
          </li>
          <li class="facebox-user-list-item">
            <a class="d-inline-block" data-hovercard-user-id="19036496" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/terryjreedy"><img src="https://avatars2.githubusercontent.com/u/19036496?s=48&amp;v=4" width="24" height="24" alt="@terryjreedy" /></a>
            <a data-hovercard-user-id="19036496" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/terryjreedy">terryjreedy</a>
          </li>
          <li class="facebox-user-list-item">
            <a class="d-inline-block" data-hovercard-user-id="355822" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/cjerdonek"><img src="https://avatars3.githubusercontent.com/u/355822?s=48&amp;v=4" width="24" height="24" alt="@cjerdonek" /></a>
            <a data-hovercard-user-id="355822" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/cjerdonek">cjerdonek</a>
          </li>
          <li class="facebox-user-list-item">
            <a class="d-inline-block" data-hovercard-user-id="3659035" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/serhiy-storchaka"><img src="https://avatars1.githubusercontent.com/u/3659035?s=48&amp;v=4" width="24" height="24" alt="@serhiy-storchaka" /></a>
            <a data-hovercard-user-id="3659035" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/serhiy-storchaka">serhiy-storchaka</a>
          </li>
          <li class="facebox-user-list-item">
            <a class="d-inline-block" data-hovercard-user-id="142113" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/florentx"><img src="https://avatars2.githubusercontent.com/u/142113?s=48&amp;v=4" width="24" height="24" alt="@florentx" /></a>
            <a data-hovercard-user-id="142113" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/florentx">florentx</a>
          </li>
          <li class="facebox-user-list-item">
            <a class="d-inline-block" data-hovercard-user-id="588792" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/freddrake"><img src="https://avatars1.githubusercontent.com/u/588792?s=48&amp;v=4" width="24" height="24" alt="@freddrake" /></a>
            <a data-hovercard-user-id="588792" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/freddrake">freddrake</a>
          </li>
          <li class="facebox-user-list-item">
            <a class="d-inline-block" data-hovercard-user-id="210184" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/warsaw"><img src="https://avatars1.githubusercontent.com/u/210184?s=48&amp;v=4" width="24" height="24" alt="@warsaw" /></a>
            <a data-hovercard-user-id="210184" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/warsaw">warsaw</a>
          </li>
          <li class="facebox-user-list-item">
            <a class="d-inline-block" data-hovercard-user-id="70927" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/akheron"><img src="https://avatars1.githubusercontent.com/u/70927?s=48&amp;v=4" width="24" height="24" alt="@akheron" /></a>
            <a data-hovercard-user-id="70927" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/akheron">akheron</a>
          </li>
          <li class="facebox-user-list-item">
            <a class="d-inline-block" data-hovercard-user-id="3646926" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/elenaoat"><img src="https://avatars0.githubusercontent.com/u/3646926?s=48&amp;v=4" width="24" height="24" alt="@elenaoat" /></a>
            <a data-hovercard-user-id="3646926" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/elenaoat">elenaoat</a>
          </li>
          <li class="facebox-user-list-item">
            <a class="d-inline-block" data-hovercard-user-id="148100" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/invalid-email-address"><img src="https://avatars3.githubusercontent.com/u/148100?s=48&amp;v=4" width="24" height="24" alt="@invalid-email-address" /></a>
            <a data-hovercard-user-id="148100" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/invalid-email-address">invalid-email-address</a>
          </li>
          <li class="facebox-user-list-item">
            <a class="d-inline-block" data-hovercard-user-id="5833005" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/ned-deily"><img src="https://avatars1.githubusercontent.com/u/5833005?s=48&amp;v=4" width="24" height="24" alt="@ned-deily" /></a>
            <a data-hovercard-user-id="5833005" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/ned-deily">ned-deily</a>
          </li>
          <li class="facebox-user-list-item">
            <a class="d-inline-block" data-hovercard-user-id="11985251" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/suic86"><img src="https://avatars3.githubusercontent.com/u/11985251?s=48&amp;v=4" width="24" height="24" alt="@suic86" /></a>
            <a data-hovercard-user-id="11985251" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/suic86">suic86</a>
          </li>
          <li class="facebox-user-list-item">
            <a class="d-inline-block" data-hovercard-user-id="239510" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/JulienPalard"><img src="https://avatars0.githubusercontent.com/u/239510?s=48&amp;v=4" width="24" height="24" alt="@JulienPalard" /></a>
            <a data-hovercard-user-id="239510" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/JulienPalard">JulienPalard</a>
          </li>
          <li class="facebox-user-list-item">
            <a class="d-inline-block" data-hovercard-user-id="145979" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/dstufft"><img src="https://avatars2.githubusercontent.com/u/145979?s=48&amp;v=4" width="24" height="24" alt="@dstufft" /></a>
            <a data-hovercard-user-id="145979" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/dstufft">dstufft</a>
          </li>
          <li class="facebox-user-list-item">
            <a class="d-inline-block" data-hovercard-user-id="1810591" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/asottile"><img src="https://avatars2.githubusercontent.com/u/1810591?s=48&amp;v=4" width="24" height="24" alt="@asottile" /></a>
            <a data-hovercard-user-id="1810591" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/asottile">asottile</a>
          </li>
      </ul>
    </div>
  </div>



  <div class="file">
    <div class="file-header">
  <div class="file-actions">

    <div class="BtnGroup">
      <a id="raw-url" class="btn btn-sm BtnGroup-item" href="/python/cpython/raw/master/Doc/library/argparse.rst">Raw</a>
        <a class="btn btn-sm js-update-url-with-hash BtnGroup-item" data-hotkey="b" href="/python/cpython/blame/master/Doc/library/argparse.rst">Blame</a>
      <a rel="nofollow" class="btn btn-sm BtnGroup-item" href="/python/cpython/commits/master/Doc/library/argparse.rst">History</a>
    </div>


          <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="inline-form js-update-url-with-hash" action="/python/cpython/edit/master/Doc/library/argparse.rst" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="eMrLhvzumY/IGgrMmqwDPYs6Xgow3/aZfSxIll8EeRMobZkl1GLckf5BR12svO6OVSnwKuIHI118MNCoqtHH5A==" />
            <button class="btn-octicon tooltipped tooltipped-nw" type="submit"
              aria-label="Fork this project and edit the file" data-hotkey="e" data-disable-with>
              <svg class="octicon octicon-pencil" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M0 12v3h3l8-8-3-3-8 8zm3 2H1v-2h1v1h1v1zm10.3-9.3L12 6 9 3l1.3-1.3a.996.996 0 0 1 1.41 0l1.59 1.59c.39.39.39 1.02 0 1.41z"/></svg>
            </button>
</form>
        <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="inline-form" action="/python/cpython/delete/master/Doc/library/argparse.rst" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="MsBTyKcXy+KNRTnfrq1u3IgndVRoK2kDqV6Z5loYxtHqNDeomZdeW/OmunKIHe47FFzoJbQPLWHAd5K0neKG5A==" />
          <button class="btn-octicon btn-octicon-danger tooltipped tooltipped-nw" type="submit"
            aria-label="Fork this project and delete the file" data-disable-with>
            <svg class="octicon octicon-trashcan" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M11 2H9c0-.55-.45-1-1-1H5c-.55 0-1 .45-1 1H2c-.55 0-1 .45-1 1v1c0 .55.45 1 1 1v9c0 .55.45 1 1 1h7c.55 0 1-.45 1-1V5c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm-1 12H3V5h1v8h1V5h1v8h1V5h1v8h1V5h1v9zm1-10H2V3h9v1z"/></svg>
          </button>
</form>  </div>

  <div class="file-info">
      2084 lines (1567 sloc)
      <span class="file-info-divider"></span>
    77.3 KB
  </div>
</div>

    
  <div id="readme" class="readme blob instapaper_body">
    <article class="markdown-body entry-content" itemprop="text"><h1><a id="user-content-modargparse-----parser-for-command-line-options-arguments-and-sub-commands" class="anchor" aria-hidden="true" href="#modargparse-----parser-for-command-line-options-arguments-and-sub-commands"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><a href="#id1">:mod:`argparse`</a> --- Parser for command-line options, arguments and sub-commands</h1>
<pre>.. module:: argparse
   :synopsis: Command-line option and argument parsing library.

</pre>
<pre>.. moduleauthor:: Steven Bethard &lt;steven.bethard@gmail.com&gt;
</pre>
<pre>.. sectionauthor:: Steven Bethard &lt;steven.bethard@gmail.com&gt;

</pre>
<pre>.. versionadded:: 3.2

</pre>
<p><strong>Source code:</strong> <a href="#id3">:source:`Lib/argparse.py`</a></p>
<hr>
<div>
<p>Tutorial</p>
<p>This page contains the API reference information. For a more gentle
introduction to Python command-line parsing, have a look at the
<a href="#id5">:ref:`argparse tutorial &lt;argparse-tutorial&gt;`</a>.</p>
</div>
<p>The <a href="#id7">:mod:`argparse`</a> module makes it easy to write user-friendly command-line
interfaces. The program defines what arguments it requires, and <a href="#id9">:mod:`argparse`</a>
will figure out how to parse those out of <a href="#id11">:data:`sys.argv`</a>.  The <a href="#id13">:mod:`argparse`</a>
module also automatically generates help and usage messages and issues errors
when users give the program invalid arguments.</p>
<a name="user-content-example"></a>
<h2><a id="user-content-example" class="anchor" aria-hidden="true" href="#example"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Example</h2>
<p>The following code is a Python program that takes a list of integers and
produces either the sum or the max:</p>
<pre>import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))
</pre>
<p>Assuming the Python code above is saved into a file called <code>prog.py</code>, it can
be run at the command line and provides useful help messages:</p>
<pre lang="shell-session">$ python prog.py -h
usage: prog.py [-h] [--sum] N [N ...]

Process some integers.

positional arguments:
 N           an integer for the accumulator

optional arguments:
 -h, --help  show this help message and exit
 --sum       sum the integers (default: find the max)
</pre>
<p>When run with the appropriate arguments, it prints either the sum or the max of
the command-line integers:</p>
<pre lang="shell-session">$ python prog.py 1 2 3 4
4

$ python prog.py 1 2 3 4 --sum
10
</pre>
<p>If invalid arguments are passed in, it will issue an error:</p>
<pre lang="shell-session">$ python prog.py a b c
usage: prog.py [-h] [--sum] N [N ...]
prog.py: error: argument N: invalid int value: 'a'
</pre>
<p>The following sections walk you through this example.</p>
<a name="user-content-creating-a-parser"></a>
<h3><a id="user-content-creating-a-parser" class="anchor" aria-hidden="true" href="#creating-a-parser"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Creating a parser</h3>
<p>The first step in using the <a href="#id15">:mod:`argparse`</a> is creating an
<a href="#id17">:class:`ArgumentParser`</a> object:</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser(description='Process some integers.')
</pre>
<p>The <a href="#id19">:class:`ArgumentParser`</a> object will hold all the information necessary to
parse the command line into Python data types.</p>
<a name="user-content-adding-arguments"></a>
<h3><a id="user-content-adding-arguments" class="anchor" aria-hidden="true" href="#adding-arguments"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Adding arguments</h3>
<p>Filling an <a href="#id21">:class:`ArgumentParser`</a> with information about program arguments is
done by making calls to the <a href="#id23">:meth:`~ArgumentParser.add_argument`</a> method.
Generally, these calls tell the <a href="#id25">:class:`ArgumentParser`</a> how to take the strings
on the command line and turn them into objects.  This information is stored and
used when <a href="#id27">:meth:`~ArgumentParser.parse_args`</a> is called. For example:</p>
<pre>&gt;&gt;&gt; parser.add_argument('integers', metavar='N', type=int, nargs='+',
...                     help='an integer for the accumulator')
&gt;&gt;&gt; parser.add_argument('--sum', dest='accumulate', action='store_const',
...                     const=sum, default=max,
...                     help='sum the integers (default: find the max)')
</pre>
<p>Later, calling <a href="#id29">:meth:`~ArgumentParser.parse_args`</a> will return an object with
two attributes, <code>integers</code> and <code>accumulate</code>.  The <code>integers</code> attribute
will be a list of one or more ints, and the <code>accumulate</code> attribute will be
either the <a href="#id31">:func:`sum`</a> function, if <code>--sum</code> was specified at the command line,
or the <a href="#id33">:func:`max`</a> function if it was not.</p>
<a name="user-content-parsing-arguments"></a>
<h3><a id="user-content-parsing-arguments" class="anchor" aria-hidden="true" href="#parsing-arguments"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Parsing arguments</h3>
<p><a href="#id35">:class:`ArgumentParser`</a> parses arguments through the
<a href="#id37">:meth:`~ArgumentParser.parse_args`</a> method.  This will inspect the command line,
convert each argument to the appropriate type and then invoke the appropriate action.
In most cases, this means a simple <a href="#id39">:class:`Namespace`</a> object will be built up from
attributes parsed out of the command line:</p>
<pre>&gt;&gt;&gt; parser.parse_args(['--sum', '7', '-1', '42'])
Namespace(accumulate=&lt;built-in function sum&gt;, integers=[7, -1, 42])
</pre>
<p>In a script, <a href="#id41">:meth:`~ArgumentParser.parse_args`</a> will typically be called with no
arguments, and the <a href="#id43">:class:`ArgumentParser`</a> will automatically determine the
command-line arguments from <a href="#id45">:data:`sys.argv`</a>.</p>
<a name="user-content-argumentparser-objects"></a>
<h2><a id="user-content-argumentparser-objects" class="anchor" aria-hidden="true" href="#argumentparser-objects"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>ArgumentParser objects</h2>
<p>The following sections describe how each of these are used.</p>
<a name="user-content-prog"></a>
<h3><a id="user-content-prog" class="anchor" aria-hidden="true" href="#prog"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>prog</h3>
<p>By default, <a href="#id47">:class:`ArgumentParser`</a> objects use <code>sys.argv[0]</code> to determine
how to display the name of the program in help messages.  This default is almost
always desirable because it will make the help messages match how the program was
invoked on the command line.  For example, consider a file named
<code>myprogram.py</code> with the following code:</p>
<pre>import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--foo', help='foo help')
args = parser.parse_args()
</pre>
<p>The help for this program will display <code>myprogram.py</code> as the program name
(regardless of where the program was invoked from):</p>
<pre lang="shell-session">$ python myprogram.py --help
usage: myprogram.py [-h] [--foo FOO]

optional arguments:
 -h, --help  show this help message and exit
 --foo FOO   foo help
$ cd ..
$ python subdir/myprogram.py --help
usage: myprogram.py [-h] [--foo FOO]

optional arguments:
 -h, --help  show this help message and exit
 --foo FOO   foo help
</pre>
<p>To change this default behavior, another value can be supplied using the
<code>prog=</code> argument to <a href="#id49">:class:`ArgumentParser`</a>:</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser(prog='myprogram')
&gt;&gt;&gt; parser.print_help()
usage: myprogram [-h]

optional arguments:
 -h, --help  show this help message and exit
</pre>
<p>Note that the program name, whether determined from <code>sys.argv[0]</code> or from the
<code>prog=</code> argument, is available to help messages using the <code>%(prog)s</code> format
specifier.</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser(prog='myprogram')
&gt;&gt;&gt; parser.add_argument('--foo', help='foo of the %(prog)s program')
&gt;&gt;&gt; parser.print_help()
usage: myprogram [-h] [--foo FOO]

optional arguments:
 -h, --help  show this help message and exit
 --foo FOO   foo of the myprogram program
</pre>
<a name="user-content-usage"></a>
<h3><a id="user-content-usage" class="anchor" aria-hidden="true" href="#usage"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>usage</h3>
<p>By default, <a href="#id51">:class:`ArgumentParser`</a> calculates the usage message from the
arguments it contains:</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser(prog='PROG')
&gt;&gt;&gt; parser.add_argument('--foo', nargs='?', help='foo help')
&gt;&gt;&gt; parser.add_argument('bar', nargs='+', help='bar help')
&gt;&gt;&gt; parser.print_help()
usage: PROG [-h] [--foo [FOO]] bar [bar ...]

positional arguments:
 bar          bar help

optional arguments:
 -h, --help   show this help message and exit
 --foo [FOO]  foo help
</pre>
<p>The default message can be overridden with the <code>usage=</code> keyword argument:</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser(prog='PROG', usage='%(prog)s [options]')
&gt;&gt;&gt; parser.add_argument('--foo', nargs='?', help='foo help')
&gt;&gt;&gt; parser.add_argument('bar', nargs='+', help='bar help')
&gt;&gt;&gt; parser.print_help()
usage: PROG [options]

positional arguments:
 bar          bar help

optional arguments:
 -h, --help   show this help message and exit
 --foo [FOO]  foo help
</pre>
<p>The <code>%(prog)s</code> format specifier is available to fill in the program name in
your usage messages.</p>
<a name="user-content-description"></a>
<h3><a id="user-content-description" class="anchor" aria-hidden="true" href="#description"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>description</h3>
<p>Most calls to the <a href="#id53">:class:`ArgumentParser`</a> constructor will use the
<code>description=</code> keyword argument.  This argument gives a brief description of
what the program does and how it works.  In help messages, the description is
displayed between the command-line usage string and the help messages for the
various arguments:</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser(description='A foo that bars')
&gt;&gt;&gt; parser.print_help()
usage: argparse.py [-h]

A foo that bars

optional arguments:
 -h, --help  show this help message and exit
</pre>
<p>By default, the description will be line-wrapped so that it fits within the
given space.  To change this behavior, see the <a href="#formatter-class">formatter_class</a> argument.</p>
<a name="user-content-epilog"></a>
<h3><a id="user-content-epilog" class="anchor" aria-hidden="true" href="#epilog"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>epilog</h3>
<p>Some programs like to display additional description of the program after the
description of the arguments.  Such text can be specified using the <code>epilog=</code>
argument to <a href="#id55">:class:`ArgumentParser`</a>:</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser(
...     description='A foo that bars',
...     epilog="And that's how you'd foo a bar")
&gt;&gt;&gt; parser.print_help()
usage: argparse.py [-h]

A foo that bars

optional arguments:
 -h, --help  show this help message and exit

And that's how you'd foo a bar
</pre>
<p>As with the <a href="#description">description</a> argument, the <code>epilog=</code> text is by default
line-wrapped, but this behavior can be adjusted with the <a href="#formatter-class">formatter_class</a>
argument to <a href="#id57">:class:`ArgumentParser`</a>.</p>
<a name="user-content-parents"></a>
<h3><a id="user-content-parents" class="anchor" aria-hidden="true" href="#parents"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>parents</h3>
<p>Sometimes, several parsers share a common set of arguments. Rather than
repeating the definitions of these arguments, a single parser with all the
shared arguments and passed to <code>parents=</code> argument to <a href="#id59">:class:`ArgumentParser`</a>
can be used.  The <code>parents=</code> argument takes a list of <a href="#id61">:class:`ArgumentParser`</a>
objects, collects all the positional and optional actions from them, and adds
these actions to the <a href="#id63">:class:`ArgumentParser`</a> object being constructed:</p>
<pre>&gt;&gt;&gt; parent_parser = argparse.ArgumentParser(add_help=False)
&gt;&gt;&gt; parent_parser.add_argument('--parent', type=int)

&gt;&gt;&gt; foo_parser = argparse.ArgumentParser(parents=[parent_parser])
&gt;&gt;&gt; foo_parser.add_argument('foo')
&gt;&gt;&gt; foo_parser.parse_args(['--parent', '2', 'XXX'])
Namespace(foo='XXX', parent=2)

&gt;&gt;&gt; bar_parser = argparse.ArgumentParser(parents=[parent_parser])
&gt;&gt;&gt; bar_parser.add_argument('--bar')
&gt;&gt;&gt; bar_parser.parse_args(['--bar', 'YYY'])
Namespace(bar='YYY', parent=None)
</pre>
<p>Note that most parent parsers will specify <code>add_help=False</code>.  Otherwise, the
<a href="#id65">:class:`ArgumentParser`</a> will see two <code>-h/--help</code> options (one in the parent
and one in the child) and raise an error.</p>
<div>
<p>Note</p>
<p>You must fully initialize the parsers before passing them via <code>parents=</code>.
If you change the parent parsers after the child parser, those changes will
not be reflected in the child.</p>
</div>
<a name="user-content-formatter-class"></a>
<h3><a id="user-content-formatter_class" class="anchor" aria-hidden="true" href="#formatter_class"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>formatter_class</h3>
<p><a href="#id67">:class:`ArgumentParser`</a> objects allow the help formatting to be customized by
specifying an alternate formatting class.  Currently, there are four such
classes:</p>
<p><a href="#id69">:class:`RawDescriptionHelpFormatter`</a> and <a href="#id71">:class:`RawTextHelpFormatter`</a> give
more control over how textual descriptions are displayed.
By default, <a href="#id73">:class:`ArgumentParser`</a> objects line-wrap the <a href="#description">description</a> and
<a href="#epilog">epilog</a> texts in command-line help messages:</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser(
...     prog='PROG',
...     description='''this description
...         was indented weird
...             but that is okay''',
...     epilog='''
...             likewise for this epilog whose whitespace will
...         be cleaned up and whose words will be wrapped
...         across a couple lines''')
&gt;&gt;&gt; parser.print_help()
usage: PROG [-h]

this description was indented weird but that is okay

optional arguments:
 -h, --help  show this help message and exit

likewise for this epilog whose whitespace will be cleaned up and whose words
will be wrapped across a couple lines
</pre>
<p>Passing <a href="#id75">:class:`RawDescriptionHelpFormatter`</a> as <code>formatter_class=</code>
indicates that <a href="#description">description</a> and <a href="#epilog">epilog</a> are already correctly formatted and
should not be line-wrapped:</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser(
...     prog='PROG',
...     formatter_class=argparse.RawDescriptionHelpFormatter,
...     description=textwrap.dedent('''\
...         Please do not mess up this text!
...         --------------------------------
...             I have indented it
...             exactly the way
...             I want it
...         '''))
&gt;&gt;&gt; parser.print_help()
usage: PROG [-h]

Please do not mess up this text!
--------------------------------
   I have indented it
   exactly the way
   I want it

optional arguments:
 -h, --help  show this help message and exit
</pre>
<p><a href="#id77">:class:`RawTextHelpFormatter`</a> maintains whitespace for all sorts of help text,
including argument descriptions. However, multiple new lines are replaced with
one. If you wish to preserve multiple blank lines, add spaces between the
newlines.</p>
<p><a href="#id79">:class:`ArgumentDefaultsHelpFormatter`</a> automatically adds information about
default values to each of the argument help messages:</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser(
...     prog='PROG',
...     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
&gt;&gt;&gt; parser.add_argument('--foo', type=int, default=42, help='FOO!')
&gt;&gt;&gt; parser.add_argument('bar', nargs='*', default=[1, 2, 3], help='BAR!')
&gt;&gt;&gt; parser.print_help()
usage: PROG [-h] [--foo FOO] [bar [bar ...]]

positional arguments:
 bar         BAR! (default: [1, 2, 3])

optional arguments:
 -h, --help  show this help message and exit
 --foo FOO   FOO! (default: 42)
</pre>
<p><a href="#id81">:class:`MetavarTypeHelpFormatter`</a> uses the name of the <a href="#type">type</a> argument for each
argument as the display name for its values (rather than using the <a href="#dest">dest</a>
as the regular formatter does):</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser(
...     prog='PROG',
...     formatter_class=argparse.MetavarTypeHelpFormatter)
&gt;&gt;&gt; parser.add_argument('--foo', type=int)
&gt;&gt;&gt; parser.add_argument('bar', type=float)
&gt;&gt;&gt; parser.print_help()
usage: PROG [-h] [--foo int] float

positional arguments:
  float

optional arguments:
  -h, --help  show this help message and exit
  --foo int
</pre>
<a name="user-content-prefix-chars"></a>
<h3><a id="user-content-prefix_chars" class="anchor" aria-hidden="true" href="#prefix_chars"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>prefix_chars</h3>
<p>Most command-line options will use <code>-</code> as the prefix, e.g. <code>-f/--foo</code>.
Parsers that need to support different or additional prefix
characters, e.g. for options
like <code>+f</code> or <code>/foo</code>, may specify them using the <code>prefix_chars=</code> argument
to the ArgumentParser constructor:</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser(prog='PROG', prefix_chars='-+')
&gt;&gt;&gt; parser.add_argument('+f')
&gt;&gt;&gt; parser.add_argument('++bar')
&gt;&gt;&gt; parser.parse_args('+f X ++bar Y'.split())
Namespace(bar='Y', f='X')
</pre>
<p>The <code>prefix_chars=</code> argument defaults to <code>'-'</code>. Supplying a set of
characters that does not include <code>-</code> will cause <code>-f/--foo</code> options to be
disallowed.</p>
<a name="user-content-fromfile-prefix-chars"></a>
<h3><a id="user-content-fromfile_prefix_chars" class="anchor" aria-hidden="true" href="#fromfile_prefix_chars"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>fromfile_prefix_chars</h3>
<p>Sometimes, for example when dealing with a particularly long argument lists, it
may make sense to keep the list of arguments in a file rather than typing it out
at the command line.  If the <code>fromfile_prefix_chars=</code> argument is given to the
<a href="#id83">:class:`ArgumentParser`</a> constructor, then arguments that start with any of the
specified characters will be treated as files, and will be replaced by the
arguments they contain.  For example:</p>
<pre>&gt;&gt;&gt; with open('args.txt', 'w') as fp:
...     fp.write('-f\nbar')
&gt;&gt;&gt; parser = argparse.ArgumentParser(fromfile_prefix_chars='@')
&gt;&gt;&gt; parser.add_argument('-f')
&gt;&gt;&gt; parser.parse_args(['-f', 'foo', '@args.txt'])
Namespace(f='bar')
</pre>
<p>Arguments read from a file must by default be one per line (but see also
<a href="#id85">:meth:`~ArgumentParser.convert_arg_line_to_args`</a>) and are treated as if they
were in the same place as the original file referencing argument on the command
line.  So in the example above, the expression <code>['-f', 'foo', '@args.txt']</code>
is considered equivalent to the expression <code>['-f', 'foo', '-f', 'bar']</code>.</p>
<p>The <code>fromfile_prefix_chars=</code> argument defaults to <code>None</code>, meaning that
arguments will never be treated as file references.</p>
<a name="user-content-argument-default"></a>
<h3><a id="user-content-argument_default" class="anchor" aria-hidden="true" href="#argument_default"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>argument_default</h3>
<p>Generally, argument defaults are specified either by passing a default to
<a href="#id87">:meth:`~ArgumentParser.add_argument`</a> or by calling the
<a href="#id89">:meth:`~ArgumentParser.set_defaults`</a> methods with a specific set of name-value
pairs.  Sometimes however, it may be useful to specify a single parser-wide
default for arguments.  This can be accomplished by passing the
<code>argument_default=</code> keyword argument to <a href="#id91">:class:`ArgumentParser`</a>.  For example,
to globally suppress attribute creation on <a href="#id93">:meth:`~ArgumentParser.parse_args`</a>
calls, we supply <code>argument_default=SUPPRESS</code>:</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
&gt;&gt;&gt; parser.add_argument('--foo')
&gt;&gt;&gt; parser.add_argument('bar', nargs='?')
&gt;&gt;&gt; parser.parse_args(['--foo', '1', 'BAR'])
Namespace(bar='BAR', foo='1')
&gt;&gt;&gt; parser.parse_args([])
Namespace()
</pre>
<a name="user-content-id95"></a>
<h3><a id="user-content-allow_abbrev" class="anchor" aria-hidden="true" href="#allow_abbrev"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>allow_abbrev</h3>
<p>Normally, when you pass an argument list to the
<a href="#id96">:meth:`~ArgumentParser.parse_args`</a> method of an <a href="#id98">:class:`ArgumentParser`</a>,
it <a href="#id100">:ref:`recognizes abbreviations &lt;prefix-matching&gt;`</a> of long options.</p>
<p>This feature can be disabled by setting <code>allow_abbrev</code> to <code>False</code>:</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser(prog='PROG', allow_abbrev=False)
&gt;&gt;&gt; parser.add_argument('--foobar', action='store_true')
&gt;&gt;&gt; parser.add_argument('--foonley', action='store_false')
&gt;&gt;&gt; parser.parse_args(['--foon'])
usage: PROG [-h] [--foobar] [--foonley]
PROG: error: unrecognized arguments: --foon
</pre>
<pre>.. versionadded:: 3.5


</pre>
<a name="user-content-conflict-handler"></a>
<h3><a id="user-content-conflict_handler" class="anchor" aria-hidden="true" href="#conflict_handler"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>conflict_handler</h3>
<p><a href="#id102">:class:`ArgumentParser`</a> objects do not allow two actions with the same option
string.  By default, <a href="#id104">:class:`ArgumentParser`</a> objects raise an exception if an
attempt is made to create an argument with an option string that is already in
use:</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser(prog='PROG')
&gt;&gt;&gt; parser.add_argument('-f', '--foo', help='old foo help')
&gt;&gt;&gt; parser.add_argument('--foo', help='new foo help')
Traceback (most recent call last):
 ..
ArgumentError: argument --foo: conflicting option string(s): --foo
</pre>
<p>Sometimes (e.g. when using <a href="#parents">parents</a>) it may be useful to simply override any
older arguments with the same option string.  To get this behavior, the value
<code>'resolve'</code> can be supplied to the <code>conflict_handler=</code> argument of
<a href="#id106">:class:`ArgumentParser`</a>:</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser(prog='PROG', conflict_handler='resolve')
&gt;&gt;&gt; parser.add_argument('-f', '--foo', help='old foo help')
&gt;&gt;&gt; parser.add_argument('--foo', help='new foo help')
&gt;&gt;&gt; parser.print_help()
usage: PROG [-h] [-f FOO] [--foo FOO]

optional arguments:
 -h, --help  show this help message and exit
 -f FOO      old foo help
 --foo FOO   new foo help
</pre>
<p>Note that <a href="#id108">:class:`ArgumentParser`</a> objects only remove an action if all of its
option strings are overridden.  So, in the example above, the old <code>-f/--foo</code>
action is retained as the <code>-f</code> action, because only the <code>--foo</code> option
string was overridden.</p>
<a name="user-content-add-help"></a>
<h3><a id="user-content-add_help" class="anchor" aria-hidden="true" href="#add_help"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>add_help</h3>
<p>By default, ArgumentParser objects add an option which simply displays
the parser's help message. For example, consider a file named
<code>myprogram.py</code> containing the following code:</p>
<pre>import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--foo', help='foo help')
args = parser.parse_args()
</pre>
<p>If <code>-h</code> or <code>--help</code> is supplied at the command line, the ArgumentParser
help will be printed:</p>
<pre lang="shell-session">$ python myprogram.py --help
usage: myprogram.py [-h] [--foo FOO]

optional arguments:
 -h, --help  show this help message and exit
 --foo FOO   foo help
</pre>
<p>Occasionally, it may be useful to disable the addition of this help option.
This can be achieved by passing <code>False</code> as the <code>add_help=</code> argument to
<a href="#id110">:class:`ArgumentParser`</a>:</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser(prog='PROG', add_help=False)
&gt;&gt;&gt; parser.add_argument('--foo', help='foo help')
&gt;&gt;&gt; parser.print_help()
usage: PROG [--foo FOO]

optional arguments:
 --foo FOO  foo help
</pre>
<p>The help option is typically <code>-h/--help</code>. The exception to this is
if the <code>prefix_chars=</code> is specified and does not include <code>-</code>, in
which case <code>-h</code> and <code>--help</code> are not valid options.  In
this case, the first character in <code>prefix_chars</code> is used to prefix
the help options:</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser(prog='PROG', prefix_chars='+/')
&gt;&gt;&gt; parser.print_help()
usage: PROG [+h]

optional arguments:
  +h, ++help  show this help message and exit
</pre>
<a name="user-content-the-add-argument-method"></a>
<h2><a id="user-content-the-add_argument-method" class="anchor" aria-hidden="true" href="#the-add_argument-method"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>The add_argument() method</h2>
<pre>.. method:: ArgumentParser.add_argument(name or flags..., [action], [nargs], \
                           [const], [default], [type], [choices], [required], \
                           [help], [metavar], [dest])

   Define how a single command-line argument should be parsed.  Each parameter
   has its own more detailed description below, but in short they are:

   * `name or flags`_ - Either a name or a list of option strings, e.g. ``foo``
     or ``-f, --foo``.

   * action_ - The basic type of action to be taken when this argument is
     encountered at the command line.

   * nargs_ - The number of command-line arguments that should be consumed.

   * const_ - A constant value required by some action_ and nargs_ selections.

   * default_ - The value produced if the argument is absent from the
     command line.

   * type_ - The type to which the command-line argument should be converted.

   * choices_ - A container of the allowable values for the argument.

   * required_ - Whether or not the command-line option may be omitted
     (optionals only).

   * help_ - A brief description of what the argument does.

   * metavar_ - A name for the argument in usage messages.

   * dest_ - The name of the attribute to be added to the object returned by
     :meth:`parse_args`.

</pre>
<p>The following sections describe how each of these are used.</p>
<a name="user-content-name-or-flags"></a>
<h3><a id="user-content-name-or-flags" class="anchor" aria-hidden="true" href="#name-or-flags"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>name or flags</h3>
<p>The <a href="#id112">:meth:`~ArgumentParser.add_argument`</a> method must know whether an optional
argument, like <code>-f</code> or <code>--foo</code>, or a positional argument, like a list of
filenames, is expected.  The first arguments passed to
<a href="#id114">:meth:`~ArgumentParser.add_argument`</a> must therefore be either a series of
flags, or a simple argument name.  For example, an optional argument could
be created like:</p>
<pre>&gt;&gt;&gt; parser.add_argument('-f', '--foo')
</pre>
<p>while a positional argument could be created like:</p>
<pre>&gt;&gt;&gt; parser.add_argument('bar')
</pre>
<p>When <a href="#id116">:meth:`~ArgumentParser.parse_args`</a> is called, optional arguments will be
identified by the <code>-</code> prefix, and the remaining arguments will be assumed to
be positional:</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser(prog='PROG')
&gt;&gt;&gt; parser.add_argument('-f', '--foo')
&gt;&gt;&gt; parser.add_argument('bar')
&gt;&gt;&gt; parser.parse_args(['BAR'])
Namespace(bar='BAR', foo=None)
&gt;&gt;&gt; parser.parse_args(['BAR', '--foo', 'FOO'])
Namespace(bar='BAR', foo='FOO')
&gt;&gt;&gt; parser.parse_args(['--foo', 'FOO'])
usage: PROG [-h] [-f FOO] bar
PROG: error: the following arguments are required: bar
</pre>
<a name="user-content-action"></a>
<h3><a id="user-content-action" class="anchor" aria-hidden="true" href="#action"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>action</h3>
<p><a href="#id118">:class:`ArgumentParser`</a> objects associate command-line arguments with actions.  These
actions can do just about anything with the command-line arguments associated with
them, though most actions simply add an attribute to the object returned by
<a href="#id120">:meth:`~ArgumentParser.parse_args`</a>.  The <code>action</code> keyword argument specifies
how the command-line arguments should be handled. The supplied actions are:</p>
<ul>
<li><p><code>'store'</code> - This just stores the argument's value.  This is the default
action. For example:</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser()
&gt;&gt;&gt; parser.add_argument('--foo')
&gt;&gt;&gt; parser.parse_args('--foo 1'.split())
Namespace(foo='1')
</pre>
</li>
<li><p><code>'store_const'</code> - This stores the value specified by the <a href="#const">const</a> keyword
argument.  The <code>'store_const'</code> action is most commonly used with
optional arguments that specify some sort of flag.  For example:</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser()
&gt;&gt;&gt; parser.add_argument('--foo', action='store_const', const=42)
&gt;&gt;&gt; parser.parse_args(['--foo'])
Namespace(foo=42)
</pre>
</li>
<li><p><code>'store_true'</code> and <code>'store_false'</code> - These are special cases of
<code>'store_const'</code> used for storing the values <code>True</code> and <code>False</code>
respectively.  In addition, they create default values of <code>False</code> and
<code>True</code> respectively.  For example:</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser()
&gt;&gt;&gt; parser.add_argument('--foo', action='store_true')
&gt;&gt;&gt; parser.add_argument('--bar', action='store_false')
&gt;&gt;&gt; parser.add_argument('--baz', action='store_false')
&gt;&gt;&gt; parser.parse_args('--foo --bar'.split())
Namespace(foo=True, bar=False, baz=True)
</pre>
</li>
<li><p><code>'append'</code> - This stores a list, and appends each argument value to the
list.  This is useful to allow an option to be specified multiple times.
Example usage:</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser()
&gt;&gt;&gt; parser.add_argument('--foo', action='append')
&gt;&gt;&gt; parser.parse_args('--foo 1 --foo 2'.split())
Namespace(foo=['1', '2'])
</pre>
</li>
<li><p><code>'append_const'</code> - This stores a list, and appends the value specified by
the <a href="#const">const</a> keyword argument to the list.  (Note that the <a href="#const">const</a> keyword
argument defaults to <code>None</code>.)  The <code>'append_const'</code> action is typically
useful when multiple arguments need to store constants to the same list. For
example:</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser()
&gt;&gt;&gt; parser.add_argument('--str', dest='types', action='append_const', const=str)
&gt;&gt;&gt; parser.add_argument('--int', dest='types', action='append_const', const=int)
&gt;&gt;&gt; parser.parse_args('--str --int'.split())
Namespace(types=[&lt;class 'str'&gt;, &lt;class 'int'&gt;])
</pre>
</li>
<li><p><code>'count'</code> - This counts the number of times a keyword argument occurs. For
example, this is useful for increasing verbosity levels:</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser()
&gt;&gt;&gt; parser.add_argument('--verbose', '-v', action='count')
&gt;&gt;&gt; parser.parse_args(['-vvv'])
Namespace(verbose=3)
</pre>
</li>
<li><p><code>'help'</code> - This prints a complete help message for all the options in the
current parser and then exits. By default a help action is automatically
added to the parser. See <a href="#id122">:class:`ArgumentParser`</a> for details of how the
output is created.</p>
</li>
<li><p><code>'version'</code> - This expects a <code>version=</code> keyword argument in the
<a href="#id124">:meth:`~ArgumentParser.add_argument`</a> call, and prints version information
and exits when invoked:</p>
<pre>&gt;&gt;&gt; import argparse
&gt;&gt;&gt; parser = argparse.ArgumentParser(prog='PROG')
&gt;&gt;&gt; parser.add_argument('--version', action='version', version='%(prog)s 2.0')
&gt;&gt;&gt; parser.parse_args(['--version'])
PROG 2.0
</pre>
</li>
</ul>
<p>You may also specify an arbitrary action by passing an Action subclass or
other object that implements the same interface.  The recommended way to do
this is to extend <a href="#id126">:class:`Action`</a>, overriding the <code>__call__</code> method
and optionally the <code>__init__</code> method.</p>
<p>An example of a custom action:</p>
<pre>&gt;&gt;&gt; class FooAction(argparse.Action):
...     def __init__(self, option_strings, dest, nargs=None, **kwargs):
...         if nargs is not None:
...             raise ValueError("nargs not allowed")
...         super(FooAction, self).__init__(option_strings, dest, **kwargs)
...     def __call__(self, parser, namespace, values, option_string=None):
...         print('%r %r %r' % (namespace, values, option_string))
...         setattr(namespace, self.dest, values)
...
&gt;&gt;&gt; parser = argparse.ArgumentParser()
&gt;&gt;&gt; parser.add_argument('--foo', action=FooAction)
&gt;&gt;&gt; parser.add_argument('bar', action=FooAction)
&gt;&gt;&gt; args = parser.parse_args('1 --foo 2'.split())
Namespace(bar=None, foo=None) '1' None
Namespace(bar='1', foo=None) '2' '--foo'
&gt;&gt;&gt; args
Namespace(bar='1', foo='2')
</pre>
<p>For more details, see <a href="#id128">:class:`Action`</a>.</p>
<a name="user-content-nargs"></a>
<h3><a id="user-content-nargs" class="anchor" aria-hidden="true" href="#nargs"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>nargs</h3>
<p>ArgumentParser objects usually associate a single command-line argument with a
single action to be taken.  The <code>nargs</code> keyword argument associates a
different number of command-line arguments with a single action.  The supported
values are:</p>
<ul>
<li><p><code>N</code> (an integer).  <code>N</code> arguments from the command line will be gathered
together into a list.  For example:</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser()
&gt;&gt;&gt; parser.add_argument('--foo', nargs=2)
&gt;&gt;&gt; parser.add_argument('bar', nargs=1)
&gt;&gt;&gt; parser.parse_args('c --foo a b'.split())
Namespace(bar=['c'], foo=['a', 'b'])
</pre>
<p>Note that <code>nargs=1</code> produces a list of one item.  This is different from
the default, in which the item is produced by itself.</p>
</li>
<li><p><code>'?'</code>. One argument will be consumed from the command line if possible, and
produced as a single item.  If no command-line argument is present, the value from
<a href="#default">default</a> will be produced.  Note that for optional arguments, there is an
additional case - the option string is present but not followed by a
command-line argument.  In this case the value from <a href="#const">const</a> will be produced.  Some
examples to illustrate this:</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser()
&gt;&gt;&gt; parser.add_argument('--foo', nargs='?', const='c', default='d')
&gt;&gt;&gt; parser.add_argument('bar', nargs='?', default='d')
&gt;&gt;&gt; parser.parse_args(['XX', '--foo', 'YY'])
Namespace(bar='XX', foo='YY')
&gt;&gt;&gt; parser.parse_args(['XX', '--foo'])
Namespace(bar='XX', foo='c')
&gt;&gt;&gt; parser.parse_args([])
Namespace(bar='d', foo='d')
</pre>
<p>One of the more common uses of <code>nargs='?'</code> is to allow optional input and
output files:</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser()
&gt;&gt;&gt; parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
...                     default=sys.stdin)
&gt;&gt;&gt; parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'),
...                     default=sys.stdout)
&gt;&gt;&gt; parser.parse_args(['input.txt', 'output.txt'])
Namespace(infile=&lt;_io.TextIOWrapper name='input.txt' encoding='UTF-8'&gt;,
          outfile=&lt;_io.TextIOWrapper name='output.txt' encoding='UTF-8'&gt;)
&gt;&gt;&gt; parser.parse_args([])
Namespace(infile=&lt;_io.TextIOWrapper name='&lt;stdin&gt;' encoding='UTF-8'&gt;,
          outfile=&lt;_io.TextIOWrapper name='&lt;stdout&gt;' encoding='UTF-8'&gt;)
</pre>
</li>
<li><p><code>'*'</code>.  All command-line arguments present are gathered into a list.  Note that
it generally doesn't make much sense to have more than one positional argument
with <code>nargs='*'</code>, but multiple optional arguments with <code>nargs='*'</code> is
possible.  For example:</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser()
&gt;&gt;&gt; parser.add_argument('--foo', nargs='*')
&gt;&gt;&gt; parser.add_argument('--bar', nargs='*')
&gt;&gt;&gt; parser.add_argument('baz', nargs='*')
&gt;&gt;&gt; parser.parse_args('a b --foo x y --bar 1 2'.split())
Namespace(bar=['1', '2'], baz=['a', 'b'], foo=['x', 'y'])
</pre>
</li>
<li><p><code>'+'</code>. Just like <code>'*'</code>, all command-line args present are gathered into a
list.  Additionally, an error message will be generated if there wasn't at
least one command-line argument present.  For example:</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser(prog='PROG')
&gt;&gt;&gt; parser.add_argument('foo', nargs='+')
&gt;&gt;&gt; parser.parse_args(['a', 'b'])
Namespace(foo=['a', 'b'])
&gt;&gt;&gt; parser.parse_args([])
usage: PROG [-h] foo [foo ...]
PROG: error: the following arguments are required: foo
</pre>
</li>
</ul>
<ul id="user-content-argparse-remainder">
<li><p><code>argparse.REMAINDER</code>.  All the remaining command-line arguments are gathered
into a list.  This is commonly useful for command line utilities that dispatch
to other command line utilities:</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser(prog='PROG')
&gt;&gt;&gt; parser.add_argument('--foo')
&gt;&gt;&gt; parser.add_argument('command')
&gt;&gt;&gt; parser.add_argument('args', nargs=argparse.REMAINDER)
&gt;&gt;&gt; print(parser.parse_args('--foo B cmd --arg1 XX ZZ'.split()))
Namespace(args=['--arg1', 'XX', 'ZZ'], command='cmd', foo='B')
</pre>
</li>
</ul>
<p>If the <code>nargs</code> keyword argument is not provided, the number of arguments consumed
is determined by the <a href="#action">action</a>.  Generally this means a single command-line argument
will be consumed and a single item (not a list) will be produced.</p>
<a name="user-content-const"></a>
<h3><a id="user-content-const" class="anchor" aria-hidden="true" href="#const"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>const</h3>
<p>The <code>const</code> argument of <a href="#id130">:meth:`~ArgumentParser.add_argument`</a> is used to hold
constant values that are not read from the command line but are required for
the various <a href="#id132">:class:`ArgumentParser`</a> actions.  The two most common uses of it are:</p>
<ul>
<li>When <a href="#id134">:meth:`~ArgumentParser.add_argument`</a> is called with
<code>action='store_const'</code> or <code>action='append_const'</code>.  These actions add the
<code>const</code> value to one of the attributes of the object returned by
<a href="#id136">:meth:`~ArgumentParser.parse_args`</a>. See the <a href="#action">action</a> description for examples.</li>
<li>When <a href="#id138">:meth:`~ArgumentParser.add_argument`</a> is called with option strings
(like <code>-f</code> or <code>--foo</code>) and <code>nargs='?'</code>.  This creates an optional
argument that can be followed by zero or one command-line arguments.
When parsing the command line, if the option string is encountered with no
command-line argument following it, the value of <code>const</code> will be assumed instead.
See the <a href="#nargs">nargs</a> description for examples.</li>
</ul>
<p>With the <code>'store_const'</code> and <code>'append_const'</code> actions, the <code>const</code>
keyword argument must be given.  For other actions, it defaults to <code>None</code>.</p>
<a name="user-content-default"></a>
<h3><a id="user-content-default" class="anchor" aria-hidden="true" href="#default"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>default</h3>
<p>All optional arguments and some positional arguments may be omitted at the
command line.  The <code>default</code> keyword argument of
<a href="#id140">:meth:`~ArgumentParser.add_argument`</a>, whose value defaults to <code>None</code>,
specifies what value should be used if the command-line argument is not present.
For optional arguments, the <code>default</code> value is used when the option string
was not present at the command line:</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser()
&gt;&gt;&gt; parser.add_argument('--foo', default=42)
&gt;&gt;&gt; parser.parse_args(['--foo', '2'])
Namespace(foo='2')
&gt;&gt;&gt; parser.parse_args([])
Namespace(foo=42)
</pre>
<p>If the <code>default</code> value is a string, the parser parses the value as if it
were a command-line argument.  In particular, the parser applies any <a href="#type">type</a>
conversion argument, if provided, before setting the attribute on the
<a href="#id142">:class:`Namespace`</a> return value.  Otherwise, the parser uses the value as is:</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser()
&gt;&gt;&gt; parser.add_argument('--length', default='10', type=int)
&gt;&gt;&gt; parser.add_argument('--width', default=10.5, type=int)
&gt;&gt;&gt; parser.parse_args()
Namespace(length=10, width=10.5)
</pre>
<p>For positional arguments with <a href="#nargs">nargs</a> equal to <code>?</code> or <code>*</code>, the <code>default</code> value
is used when no command-line argument was present:</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser()
&gt;&gt;&gt; parser.add_argument('foo', nargs='?', default=42)
&gt;&gt;&gt; parser.parse_args(['a'])
Namespace(foo='a')
&gt;&gt;&gt; parser.parse_args([])
Namespace(foo=42)
</pre>
<p>Providing <code>default=argparse.SUPPRESS</code> causes no attribute to be added if the
command-line argument was not present:</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser()
&gt;&gt;&gt; parser.add_argument('--foo', default=argparse.SUPPRESS)
&gt;&gt;&gt; parser.parse_args([])
Namespace()
&gt;&gt;&gt; parser.parse_args(['--foo', '1'])
Namespace(foo='1')
</pre>
<a name="user-content-type"></a>
<h3><a id="user-content-type" class="anchor" aria-hidden="true" href="#type"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>type</h3>
<p>By default, <a href="#id144">:class:`ArgumentParser`</a> objects read command-line arguments in as simple
strings. However, quite often the command-line string should instead be
interpreted as another type, like a <a href="#id146">:class:`float`</a> or <a href="#id148">:class:`int`</a>.  The
<code>type</code> keyword argument of <a href="#id150">:meth:`~ArgumentParser.add_argument`</a> allows any
necessary type-checking and type conversions to be performed.  Common built-in
types and functions can be used directly as the value of the <code>type</code> argument:</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser()
&gt;&gt;&gt; parser.add_argument('foo', type=int)
&gt;&gt;&gt; parser.add_argument('bar', type=open)
&gt;&gt;&gt; parser.parse_args('2 temp.txt'.split())
Namespace(bar=&lt;_io.TextIOWrapper name='temp.txt' encoding='UTF-8'&gt;, foo=2)
</pre>
<p>See the section on the <a href="#default">default</a> keyword argument for information on when the
<code>type</code> argument is applied to default arguments.</p>
<p>To ease the use of various types of files, the argparse module provides the
factory FileType which takes the <code>mode=</code>, <code>bufsize=</code>, <code>encoding=</code> and
<code>errors=</code> arguments of the <a href="#id152">:func:`open`</a> function.  For example,
<code>FileType('w')</code> can be used to create a writable file:</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser()
&gt;&gt;&gt; parser.add_argument('bar', type=argparse.FileType('w'))
&gt;&gt;&gt; parser.parse_args(['out.txt'])
Namespace(bar=&lt;_io.TextIOWrapper name='out.txt' encoding='UTF-8'&gt;)
</pre>
<p><code>type=</code> can take any callable that takes a single string argument and returns
the converted value:</p>
<pre>&gt;&gt;&gt; def perfect_square(string):
...     value = int(string)
...     sqrt = math.sqrt(value)
...     if sqrt != int(sqrt):
...         msg = "%r is not a perfect square" % string
...         raise argparse.ArgumentTypeError(msg)
...     return value
...
&gt;&gt;&gt; parser = argparse.ArgumentParser(prog='PROG')
&gt;&gt;&gt; parser.add_argument('foo', type=perfect_square)
&gt;&gt;&gt; parser.parse_args(['9'])
Namespace(foo=9)
&gt;&gt;&gt; parser.parse_args(['7'])
usage: PROG [-h] foo
PROG: error: argument foo: '7' is not a perfect square
</pre>
<p>The <a href="#choices">choices</a> keyword argument may be more convenient for type checkers that
simply check against a range of values:</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser(prog='PROG')
&gt;&gt;&gt; parser.add_argument('foo', type=int, choices=range(5, 10))
&gt;&gt;&gt; parser.parse_args(['7'])
Namespace(foo=7)
&gt;&gt;&gt; parser.parse_args(['11'])
usage: PROG [-h] {5,6,7,8,9}
PROG: error: argument foo: invalid choice: 11 (choose from 5, 6, 7, 8, 9)
</pre>
<p>See the <a href="#choices">choices</a> section for more details.</p>
<a name="user-content-choices"></a>
<h3><a id="user-content-choices" class="anchor" aria-hidden="true" href="#choices"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>choices</h3>
<p>Some command-line arguments should be selected from a restricted set of values.
These can be handled by passing a container object as the <em>choices</em> keyword
argument to <a href="#id154">:meth:`~ArgumentParser.add_argument`</a>.  When the command line is
parsed, argument values will be checked, and an error message will be displayed
if the argument was not one of the acceptable values:</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser(prog='game.py')
&gt;&gt;&gt; parser.add_argument('move', choices=['rock', 'paper', 'scissors'])
&gt;&gt;&gt; parser.parse_args(['rock'])
Namespace(move='rock')
&gt;&gt;&gt; parser.parse_args(['fire'])
usage: game.py [-h] {rock,paper,scissors}
game.py: error: argument move: invalid choice: 'fire' (choose from 'rock',
'paper', 'scissors')
</pre>
<p>Note that inclusion in the <em>choices</em> container is checked after any <a href="#type">type</a>
conversions have been performed, so the type of the objects in the <em>choices</em>
container should match the <a href="#type">type</a> specified:</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser(prog='doors.py')
&gt;&gt;&gt; parser.add_argument('door', type=int, choices=range(1, 4))
&gt;&gt;&gt; print(parser.parse_args(['3']))
Namespace(door=3)
&gt;&gt;&gt; parser.parse_args(['4'])
usage: doors.py [-h] {1,2,3}
doors.py: error: argument door: invalid choice: 4 (choose from 1, 2, 3)
</pre>
<p>Any object that supports the <code>in</code> operator can be passed as the <em>choices</em>
value, so <a href="#id156">:class:`dict`</a> objects, <a href="#id158">:class:`set`</a> objects, custom containers,
etc. are all supported.</p>
<a name="user-content-required"></a>
<h3><a id="user-content-required" class="anchor" aria-hidden="true" href="#required"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>required</h3>
<p>In general, the <a href="#id160">:mod:`argparse`</a> module assumes that flags like <code>-f</code> and <code>--bar</code>
indicate <em>optional</em> arguments, which can always be omitted at the command line.
To make an option <em>required</em>, <code>True</code> can be specified for the <code>required=</code>
keyword argument to <a href="#id162">:meth:`~ArgumentParser.add_argument`</a>:</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser()
&gt;&gt;&gt; parser.add_argument('--foo', required=True)
&gt;&gt;&gt; parser.parse_args(['--foo', 'BAR'])
Namespace(foo='BAR')
&gt;&gt;&gt; parser.parse_args([])
usage: argparse.py [-h] [--foo FOO]
argparse.py: error: option --foo is required
</pre>
<p>As the example shows, if an option is marked as <code>required</code>,
<a href="#id164">:meth:`~ArgumentParser.parse_args`</a> will report an error if that option is not
present at the command line.</p>
<div>
<p>Note</p>
<p>Required options are generally considered bad form because users expect
<em>options</em> to be <em>optional</em>, and thus they should be avoided when possible.</p>
</div>
<a name="user-content-help"></a>
<h3><a id="user-content-help" class="anchor" aria-hidden="true" href="#help"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>help</h3>
<p>The <code>help</code> value is a string containing a brief description of the argument.
When a user requests help (usually by using <code>-h</code> or <code>--help</code> at the
command line), these <code>help</code> descriptions will be displayed with each
argument:</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser(prog='frobble')
&gt;&gt;&gt; parser.add_argument('--foo', action='store_true',
...                     help='foo the bars before frobbling')
&gt;&gt;&gt; parser.add_argument('bar', nargs='+',
...                     help='one of the bars to be frobbled')
&gt;&gt;&gt; parser.parse_args(['-h'])
usage: frobble [-h] [--foo] bar [bar ...]

positional arguments:
 bar     one of the bars to be frobbled

optional arguments:
 -h, --help  show this help message and exit
 --foo   foo the bars before frobbling
</pre>
<p>The <code>help</code> strings can include various format specifiers to avoid repetition
of things like the program name or the argument <a href="#default">default</a>.  The available
specifiers include the program name, <code>%(prog)s</code> and most keyword arguments to
<a href="#id166">:meth:`~ArgumentParser.add_argument`</a>, e.g. <code>%(default)s</code>, <code>%(type)s</code>, etc.:</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser(prog='frobble')
&gt;&gt;&gt; parser.add_argument('bar', nargs='?', type=int, default=42,
...                     help='the bar to %(prog)s (default: %(default)s)')
&gt;&gt;&gt; parser.print_help()
usage: frobble [-h] [bar]

positional arguments:
 bar     the bar to frobble (default: 42)

optional arguments:
 -h, --help  show this help message and exit
</pre>
<p>As the help string supports %-formatting, if you want a literal <code>%</code> to appear
in the help string, you must escape it as <code>%%</code>.</p>
<p><a href="#id168">:mod:`argparse`</a> supports silencing the help entry for certain options, by
setting the <code>help</code> value to <code>argparse.SUPPRESS</code>:</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser(prog='frobble')
&gt;&gt;&gt; parser.add_argument('--foo', help=argparse.SUPPRESS)
&gt;&gt;&gt; parser.print_help()
usage: frobble [-h]

optional arguments:
  -h, --help  show this help message and exit
</pre>
<a name="user-content-metavar"></a>
<h3><a id="user-content-metavar" class="anchor" aria-hidden="true" href="#metavar"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>metavar</h3>
<p>When <a href="#id170">:class:`ArgumentParser`</a> generates help messages, it needs some way to refer
to each expected argument.  By default, ArgumentParser objects use the <a href="#dest">dest</a>
value as the "name" of each object.  By default, for positional argument
actions, the <a href="#dest">dest</a> value is used directly, and for optional argument actions,
the <a href="#dest">dest</a> value is uppercased.  So, a single positional argument with
<code>dest='bar'</code> will be referred to as <code>bar</code>. A single
optional argument <code>--foo</code> that should be followed by a single command-line argument
will be referred to as <code>FOO</code>.  An example:</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser()
&gt;&gt;&gt; parser.add_argument('--foo')
&gt;&gt;&gt; parser.add_argument('bar')
&gt;&gt;&gt; parser.parse_args('X --foo Y'.split())
Namespace(bar='X', foo='Y')
&gt;&gt;&gt; parser.print_help()
usage:  [-h] [--foo FOO] bar

positional arguments:
 bar

optional arguments:
 -h, --help  show this help message and exit
 --foo FOO
</pre>
<p>An alternative name can be specified with <code>metavar</code>:</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser()
&gt;&gt;&gt; parser.add_argument('--foo', metavar='YYY')
&gt;&gt;&gt; parser.add_argument('bar', metavar='XXX')
&gt;&gt;&gt; parser.parse_args('X --foo Y'.split())
Namespace(bar='X', foo='Y')
&gt;&gt;&gt; parser.print_help()
usage:  [-h] [--foo YYY] XXX

positional arguments:
 XXX

optional arguments:
 -h, --help  show this help message and exit
 --foo YYY
</pre>
<p>Note that <code>metavar</code> only changes the <em>displayed</em> name - the name of the
attribute on the <a href="#id172">:meth:`~ArgumentParser.parse_args`</a> object is still determined
by the <a href="#dest">dest</a> value.</p>
<p>Different values of <code>nargs</code> may cause the metavar to be used multiple times.
Providing a tuple to <code>metavar</code> specifies a different display for each of the
arguments:</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser(prog='PROG')
&gt;&gt;&gt; parser.add_argument('-x', nargs=2)
&gt;&gt;&gt; parser.add_argument('--foo', nargs=2, metavar=('bar', 'baz'))
&gt;&gt;&gt; parser.print_help()
usage: PROG [-h] [-x X X] [--foo bar baz]

optional arguments:
 -h, --help     show this help message and exit
 -x X X
 --foo bar baz
</pre>
<a name="user-content-dest"></a>
<h3><a id="user-content-dest" class="anchor" aria-hidden="true" href="#dest"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>dest</h3>
<p>Most <a href="#id174">:class:`ArgumentParser`</a> actions add some value as an attribute of the
object returned by <a href="#id176">:meth:`~ArgumentParser.parse_args`</a>.  The name of this
attribute is determined by the <code>dest</code> keyword argument of
<a href="#id178">:meth:`~ArgumentParser.add_argument`</a>.  For positional argument actions,
<code>dest</code> is normally supplied as the first argument to
<a href="#id180">:meth:`~ArgumentParser.add_argument`</a>:</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser()
&gt;&gt;&gt; parser.add_argument('bar')
&gt;&gt;&gt; parser.parse_args(['XXX'])
Namespace(bar='XXX')
</pre>
<p>For optional argument actions, the value of <code>dest</code> is normally inferred from
the option strings.  <a href="#id182">:class:`ArgumentParser`</a> generates the value of <code>dest</code> by
taking the first long option string and stripping away the initial <code>--</code>
string.  If no long option strings were supplied, <code>dest</code> will be derived from
the first short option string by stripping the initial <code>-</code> character.  Any
internal <code>-</code> characters will be converted to <code>_</code> characters to make sure
the string is a valid attribute name.  The examples below illustrate this
behavior:</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser()
&gt;&gt;&gt; parser.add_argument('-f', '--foo-bar', '--foo')
&gt;&gt;&gt; parser.add_argument('-x', '-y')
&gt;&gt;&gt; parser.parse_args('-f 1 -x 2'.split())
Namespace(foo_bar='1', x='2')
&gt;&gt;&gt; parser.parse_args('--foo 1 -y 2'.split())
Namespace(foo_bar='1', x='2')
</pre>
<p><code>dest</code> allows a custom attribute name to be provided:</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser()
&gt;&gt;&gt; parser.add_argument('--foo', dest='bar')
&gt;&gt;&gt; parser.parse_args('--foo XXX'.split())
Namespace(bar='XXX')
</pre>
<a name="user-content-action-classes"></a>
<h3><a id="user-content-action-classes" class="anchor" aria-hidden="true" href="#action-classes"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Action classes</h3>
<p>Action classes implement the Action API, a callable which returns a callable
which processes arguments from the command-line. Any object which follows
this API may be passed as the <code>action</code> parameter to
<a href="#id184">:meth:`add_argument`</a>.</p>
<p>Action objects are used by an ArgumentParser to represent the information
needed to parse a single argument from one or more strings from the
command line. The Action class must accept the two positional arguments
plus any keyword arguments passed to <a href="#id186">:meth:`ArgumentParser.add_argument`</a>
except for the <code>action</code> itself.</p>
<p>Instances of Action (or return value of any callable to the <code>action</code>
parameter) should have attributes "dest", "option_strings", "default", "type",
"required", "help", etc. defined. The easiest way to ensure these attributes
are defined is to call <code>Action.__init__</code>.</p>
<p>Action instances should be callable, so subclasses must override the
<code>__call__</code> method, which should accept four parameters:</p>
<ul>
<li><code>parser</code> - The ArgumentParser object which contains this action.</li>
<li><code>namespace</code> - The <a href="#id188">:class:`Namespace`</a> object that will be returned by
<a href="#id190">:meth:`~ArgumentParser.parse_args`</a>.  Most actions add an attribute to this
object using <a href="#id192">:func:`setattr`</a>.</li>
<li><code>values</code> - The associated command-line arguments, with any type conversions
applied.  Type conversions are specified with the <a href="#type">type</a> keyword argument to
<a href="#id194">:meth:`~ArgumentParser.add_argument`</a>.</li>
<li><code>option_string</code> - The option string that was used to invoke this action.
The <code>option_string</code> argument is optional, and will be absent if the action
is associated with a positional argument.</li>
</ul>
<p>The <code>__call__</code> method may perform arbitrary actions, but will typically set
attributes on the <code>namespace</code> based on <code>dest</code> and <code>values</code>.</p>
<a name="user-content-the-parse-args-method"></a>
<h2><a id="user-content-the-parse_args-method" class="anchor" aria-hidden="true" href="#the-parse_args-method"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>The parse_args() method</h2>
<pre>.. method:: ArgumentParser.parse_args(args=None, namespace=None)

   Convert argument strings to objects and assign them as attributes of the
   namespace.  Return the populated namespace.

   Previous calls to :meth:`add_argument` determine exactly what objects are
   created and how they are assigned. See the documentation for
   :meth:`add_argument` for details.

   * args_ - List of strings to parse.  The default is taken from
     :data:`sys.argv`.

   * namespace_ - An object to take the attributes.  The default is a new empty
     :class:`Namespace` object.


</pre>
<a name="user-content-option-value-syntax"></a>
<h3><a id="user-content-option-value-syntax" class="anchor" aria-hidden="true" href="#option-value-syntax"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Option value syntax</h3>
<p>The <a href="#id196">:meth:`~ArgumentParser.parse_args`</a> method supports several ways of
specifying the value of an option (if it takes one).  In the simplest case, the
option and its value are passed as two separate arguments:</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser(prog='PROG')
&gt;&gt;&gt; parser.add_argument('-x')
&gt;&gt;&gt; parser.add_argument('--foo')
&gt;&gt;&gt; parser.parse_args(['-x', 'X'])
Namespace(foo=None, x='X')
&gt;&gt;&gt; parser.parse_args(['--foo', 'FOO'])
Namespace(foo='FOO', x=None)
</pre>
<p>For long options (options with names longer than a single character), the option
and value can also be passed as a single command-line argument, using <code>=</code> to
separate them:</p>
<pre>&gt;&gt;&gt; parser.parse_args(['--foo=FOO'])
Namespace(foo='FOO', x=None)
</pre>
<p>For short options (options only one character long), the option and its value
can be concatenated:</p>
<pre>&gt;&gt;&gt; parser.parse_args(['-xX'])
Namespace(foo=None, x='X')
</pre>
<p>Several short options can be joined together, using only a single <code>-</code> prefix,
as long as only the last option (or none of them) requires a value:</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser(prog='PROG')
&gt;&gt;&gt; parser.add_argument('-x', action='store_true')
&gt;&gt;&gt; parser.add_argument('-y', action='store_true')
&gt;&gt;&gt; parser.add_argument('-z')
&gt;&gt;&gt; parser.parse_args(['-xyzZ'])
Namespace(x=True, y=True, z='Z')
</pre>
<a name="user-content-invalid-arguments"></a>
<h3><a id="user-content-invalid-arguments" class="anchor" aria-hidden="true" href="#invalid-arguments"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Invalid arguments</h3>
<p>While parsing the command line, <a href="#id198">:meth:`~ArgumentParser.parse_args`</a> checks for a
variety of errors, including ambiguous options, invalid types, invalid options,
wrong number of positional arguments, etc.  When it encounters such an error,
it exits and prints the error along with a usage message:</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser(prog='PROG')
&gt;&gt;&gt; parser.add_argument('--foo', type=int)
&gt;&gt;&gt; parser.add_argument('bar', nargs='?')

&gt;&gt;&gt; # invalid type
&gt;&gt;&gt; parser.parse_args(['--foo', 'spam'])
usage: PROG [-h] [--foo FOO] [bar]
PROG: error: argument --foo: invalid int value: 'spam'

&gt;&gt;&gt; # invalid option
&gt;&gt;&gt; parser.parse_args(['--bar'])
usage: PROG [-h] [--foo FOO] [bar]
PROG: error: no such option: --bar

&gt;&gt;&gt; # wrong number of arguments
&gt;&gt;&gt; parser.parse_args(['spam', 'badger'])
usage: PROG [-h] [--foo FOO] [bar]
PROG: error: extra arguments found: badger
</pre>
<a name="user-content-arguments-containing"></a>
<h3><a id="user-content-arguments-containing--" class="anchor" aria-hidden="true" href="#arguments-containing--"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Arguments containing <code>-</code></h3>
<p>The <a href="#id200">:meth:`~ArgumentParser.parse_args`</a> method attempts to give errors whenever
the user has clearly made a mistake, but some situations are inherently
ambiguous.  For example, the command-line argument <code>-1</code> could either be an
attempt to specify an option or an attempt to provide a positional argument.
The <a href="#id202">:meth:`~ArgumentParser.parse_args`</a> method is cautious here: positional
arguments may only begin with <code>-</code> if they look like negative numbers and
there are no options in the parser that look like negative numbers:</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser(prog='PROG')
&gt;&gt;&gt; parser.add_argument('-x')
&gt;&gt;&gt; parser.add_argument('foo', nargs='?')

&gt;&gt;&gt; # no negative number options, so -1 is a positional argument
&gt;&gt;&gt; parser.parse_args(['-x', '-1'])
Namespace(foo=None, x='-1')

&gt;&gt;&gt; # no negative number options, so -1 and -5 are positional arguments
&gt;&gt;&gt; parser.parse_args(['-x', '-1', '-5'])
Namespace(foo='-5', x='-1')

&gt;&gt;&gt; parser = argparse.ArgumentParser(prog='PROG')
&gt;&gt;&gt; parser.add_argument('-1', dest='one')
&gt;&gt;&gt; parser.add_argument('foo', nargs='?')

&gt;&gt;&gt; # negative number options present, so -1 is an option
&gt;&gt;&gt; parser.parse_args(['-1', 'X'])
Namespace(foo=None, one='X')

&gt;&gt;&gt; # negative number options present, so -2 is an option
&gt;&gt;&gt; parser.parse_args(['-2'])
usage: PROG [-h] [-1 ONE] [foo]
PROG: error: no such option: -2

&gt;&gt;&gt; # negative number options present, so both -1s are options
&gt;&gt;&gt; parser.parse_args(['-1', '-1'])
usage: PROG [-h] [-1 ONE] [foo]
PROG: error: argument -1: expected one argument
</pre>
<p>If you have positional arguments that must begin with <code>-</code> and don't look
like negative numbers, you can insert the pseudo-argument <code>'--'</code> which tells
<a href="#id204">:meth:`~ArgumentParser.parse_args`</a> that everything after that is a positional
argument:</p>
<pre>&gt;&gt;&gt; parser.parse_args(['--', '-f'])
Namespace(foo='-f', one=None)
</pre>
<a name="user-content-argument-abbreviations-prefix-matching"></a>
<h3><a id="user-content-argument-abbreviations-prefix-matching" class="anchor" aria-hidden="true" href="#argument-abbreviations-prefix-matching"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Argument abbreviations (prefix matching)</h3>
<p>The <a href="#id206">:meth:`~ArgumentParser.parse_args`</a> method <a href="#id208">:ref:`by default &lt;allow_abbrev&gt;`</a>
allows long options to be abbreviated to a prefix, if the abbreviation is
unambiguous (the prefix matches a unique option):</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser(prog='PROG')
&gt;&gt;&gt; parser.add_argument('-bacon')
&gt;&gt;&gt; parser.add_argument('-badger')
&gt;&gt;&gt; parser.parse_args('-bac MMM'.split())
Namespace(bacon='MMM', badger=None)
&gt;&gt;&gt; parser.parse_args('-bad WOOD'.split())
Namespace(bacon=None, badger='WOOD')
&gt;&gt;&gt; parser.parse_args('-ba BA'.split())
usage: PROG [-h] [-bacon BACON] [-badger BADGER]
PROG: error: ambiguous option: -ba could match -badger, -bacon
</pre>
<p>An error is produced for arguments that could produce more than one options.
This feature can be disabled by setting <a href="#id210">:ref:`allow_abbrev`</a> to <code>False</code>.</p>
<a name="user-content-beyond-sys-argv"></a>
<h3><a id="user-content-beyond-sysargv" class="anchor" aria-hidden="true" href="#beyond-sysargv"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Beyond <code>sys.argv</code></h3>
<p>Sometimes it may be useful to have an ArgumentParser parse arguments other than those
of <a href="#id212">:data:`sys.argv`</a>.  This can be accomplished by passing a list of strings to
<a href="#id214">:meth:`~ArgumentParser.parse_args`</a>.  This is useful for testing at the
interactive prompt:</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser()
&gt;&gt;&gt; parser.add_argument(
...     'integers', metavar='int', type=int, choices=range(10),
...     nargs='+', help='an integer in the range 0..9')
&gt;&gt;&gt; parser.add_argument(
...     '--sum', dest='accumulate', action='store_const', const=sum,
...     default=max, help='sum the integers (default: find the max)')
&gt;&gt;&gt; parser.parse_args(['1', '2', '3', '4'])
Namespace(accumulate=&lt;built-in function max&gt;, integers=[1, 2, 3, 4])
&gt;&gt;&gt; parser.parse_args(['1', '2', '3', '4', '--sum'])
Namespace(accumulate=&lt;built-in function sum&gt;, integers=[1, 2, 3, 4])
</pre>
<a name="user-content-the-namespace-object"></a>
<h3><a id="user-content-the-namespace-object" class="anchor" aria-hidden="true" href="#the-namespace-object"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>The Namespace object</h3>
<p>Simple class used by default by <a href="#id216">:meth:`~ArgumentParser.parse_args`</a> to create
an object holding attributes and return it.</p>
<p>This class is deliberately simple, just an <a href="#id218">:class:`object`</a> subclass with a
readable string representation. If you prefer to have dict-like view of the
attributes, you can use the standard Python idiom, <a href="#id220">:func:`vars`</a>:</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser()
&gt;&gt;&gt; parser.add_argument('--foo')
&gt;&gt;&gt; args = parser.parse_args(['--foo', 'BAR'])
&gt;&gt;&gt; vars(args)
{'foo': 'BAR'}
</pre>
<p>It may also be useful to have an <a href="#id222">:class:`ArgumentParser`</a> assign attributes to an
already existing object, rather than a new <a href="#id224">:class:`Namespace`</a> object.  This can
be achieved by specifying the <code>namespace=</code> keyword argument:</p>
<pre>&gt;&gt;&gt; class C:
...     pass
...
&gt;&gt;&gt; c = C()
&gt;&gt;&gt; parser = argparse.ArgumentParser()
&gt;&gt;&gt; parser.add_argument('--foo')
&gt;&gt;&gt; parser.parse_args(args=['--foo', 'BAR'], namespace=c)
&gt;&gt;&gt; c.foo
'BAR'
</pre>
<a name="user-content-other-utilities"></a>
<h2><a id="user-content-other-utilities" class="anchor" aria-hidden="true" href="#other-utilities"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Other utilities</h2>
<a name="user-content-sub-commands"></a>
<h3><a id="user-content-sub-commands" class="anchor" aria-hidden="true" href="#sub-commands"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Sub-commands</h3>
<pre>.. method:: ArgumentParser.add_subparsers([title], [description], [prog], \
                                          [parser_class], [action], \
                                          [option_string], [dest], [required] \
                                          [help], [metavar])

   Many programs split up their functionality into a number of sub-commands,
   for example, the ``svn`` program can invoke sub-commands like ``svn
   checkout``, ``svn update``, and ``svn commit``.  Splitting up functionality
   this way can be a particularly good idea when a program performs several
   different functions which require different kinds of command-line arguments.
   :class:`ArgumentParser` supports the creation of such sub-commands with the
   :meth:`add_subparsers` method.  The :meth:`add_subparsers` method is normally
   called with no arguments and returns a special action object.  This object
   has a single method, :meth:`~ArgumentParser.add_parser`, which takes a
   command name and any :class:`ArgumentParser` constructor arguments, and
   returns an :class:`ArgumentParser` object that can be modified as usual.

   Description of parameters:

   * title - title for the sub-parser group in help output; by default
     "subcommands" if description is provided, otherwise uses title for
     positional arguments

   * description - description for the sub-parser group in help output, by
     default ``None``

   * prog - usage information that will be displayed with sub-command help,
     by default the name of the program and any positional arguments before the
     subparser argument

   * parser_class - class which will be used to create sub-parser instances, by
     default the class of the current parser (e.g. ArgumentParser)

   * action_ - the basic type of action to be taken when this argument is
     encountered at the command line

   * dest_ - name of the attribute under which sub-command name will be
     stored; by default ``None`` and no value is stored

   * required_ - Whether or not a subcommand must be provided, by default
     ``False``.

   * help_ - help for sub-parser group in help output, by default ``None``

   * metavar_ - string presenting available sub-commands in help; by default it
     is ``None`` and presents sub-commands in form {cmd1, cmd2, ..}

   Some example usage::

     &gt;&gt;&gt; # create the top-level parser
     &gt;&gt;&gt; parser = argparse.ArgumentParser(prog='PROG')
     &gt;&gt;&gt; parser.add_argument('--foo', action='store_true', help='foo help')
     &gt;&gt;&gt; subparsers = parser.add_subparsers(help='sub-command help')
     &gt;&gt;&gt;
     &gt;&gt;&gt; # create the parser for the "a" command
     &gt;&gt;&gt; parser_a = subparsers.add_parser('a', help='a help')
     &gt;&gt;&gt; parser_a.add_argument('bar', type=int, help='bar help')
     &gt;&gt;&gt;
     &gt;&gt;&gt; # create the parser for the "b" command
     &gt;&gt;&gt; parser_b = subparsers.add_parser('b', help='b help')
     &gt;&gt;&gt; parser_b.add_argument('--baz', choices='XYZ', help='baz help')
     &gt;&gt;&gt;
     &gt;&gt;&gt; # parse some argument lists
     &gt;&gt;&gt; parser.parse_args(['a', '12'])
     Namespace(bar=12, foo=False)
     &gt;&gt;&gt; parser.parse_args(['--foo', 'b', '--baz', 'Z'])
     Namespace(baz='Z', foo=True)

   Note that the object returned by :meth:`parse_args` will only contain
   attributes for the main parser and the subparser that was selected by the
   command line (and not any other subparsers).  So in the example above, when
   the ``a`` command is specified, only the ``foo`` and ``bar`` attributes are
   present, and when the ``b`` command is specified, only the ``foo`` and
   ``baz`` attributes are present.

   Similarly, when a help message is requested from a subparser, only the help
   for that particular parser will be printed.  The help message will not
   include parent parser or sibling parser messages.  (A help message for each
   subparser command, however, can be given by supplying the ``help=`` argument
   to :meth:`add_parser` as above.)

   ::

     &gt;&gt;&gt; parser.parse_args(['--help'])
     usage: PROG [-h] [--foo] {a,b} ...

     positional arguments:
       {a,b}   sub-command help
         a     a help
         b     b help

     optional arguments:
       -h, --help  show this help message and exit
       --foo   foo help

     &gt;&gt;&gt; parser.parse_args(['a', '--help'])
     usage: PROG a [-h] bar

     positional arguments:
       bar     bar help

     optional arguments:
       -h, --help  show this help message and exit

     &gt;&gt;&gt; parser.parse_args(['b', '--help'])
     usage: PROG b [-h] [--baz {X,Y,Z}]

     optional arguments:
       -h, --help     show this help message and exit
       --baz {X,Y,Z}  baz help

   The :meth:`add_subparsers` method also supports ``title`` and ``description``
   keyword arguments.  When either is present, the subparser's commands will
   appear in their own group in the help output.  For example::

     &gt;&gt;&gt; parser = argparse.ArgumentParser()
     &gt;&gt;&gt; subparsers = parser.add_subparsers(title='subcommands',
     ...                                    description='valid subcommands',
     ...                                    help='additional help')
     &gt;&gt;&gt; subparsers.add_parser('foo')
     &gt;&gt;&gt; subparsers.add_parser('bar')
     &gt;&gt;&gt; parser.parse_args(['-h'])
     usage:  [-h] {foo,bar} ...

     optional arguments:
       -h, --help  show this help message and exit

     subcommands:
       valid subcommands

       {foo,bar}   additional help

   Furthermore, ``add_parser`` supports an additional ``aliases`` argument,
   which allows multiple strings to refer to the same subparser. This example,
   like ``svn``, aliases ``co`` as a shorthand for ``checkout``::

     &gt;&gt;&gt; parser = argparse.ArgumentParser()
     &gt;&gt;&gt; subparsers = parser.add_subparsers()
     &gt;&gt;&gt; checkout = subparsers.add_parser('checkout', aliases=['co'])
     &gt;&gt;&gt; checkout.add_argument('foo')
     &gt;&gt;&gt; parser.parse_args(['co', 'bar'])
     Namespace(foo='bar')

   One particularly effective way of handling sub-commands is to combine the use
   of the :meth:`add_subparsers` method with calls to :meth:`set_defaults` so
   that each subparser knows which Python function it should execute.  For
   example::

     &gt;&gt;&gt; # sub-command functions
     &gt;&gt;&gt; def foo(args):
     ...     print(args.x * args.y)
     ...
     &gt;&gt;&gt; def bar(args):
     ...     print('((%s))' % args.z)
     ...
     &gt;&gt;&gt; # create the top-level parser
     &gt;&gt;&gt; parser = argparse.ArgumentParser()
     &gt;&gt;&gt; subparsers = parser.add_subparsers()
     &gt;&gt;&gt;
     &gt;&gt;&gt; # create the parser for the "foo" command
     &gt;&gt;&gt; parser_foo = subparsers.add_parser('foo')
     &gt;&gt;&gt; parser_foo.add_argument('-x', type=int, default=1)
     &gt;&gt;&gt; parser_foo.add_argument('y', type=float)
     &gt;&gt;&gt; parser_foo.set_defaults(func=foo)
     &gt;&gt;&gt;
     &gt;&gt;&gt; # create the parser for the "bar" command
     &gt;&gt;&gt; parser_bar = subparsers.add_parser('bar')
     &gt;&gt;&gt; parser_bar.add_argument('z')
     &gt;&gt;&gt; parser_bar.set_defaults(func=bar)
     &gt;&gt;&gt;
     &gt;&gt;&gt; # parse the args and call whatever function was selected
     &gt;&gt;&gt; args = parser.parse_args('foo 1 -x 2'.split())
     &gt;&gt;&gt; args.func(args)
     2.0
     &gt;&gt;&gt;
     &gt;&gt;&gt; # parse the args and call whatever function was selected
     &gt;&gt;&gt; args = parser.parse_args('bar XYZYX'.split())
     &gt;&gt;&gt; args.func(args)
     ((XYZYX))

   This way, you can let :meth:`parse_args` do the job of calling the
   appropriate function after argument parsing is complete.  Associating
   functions with actions like this is typically the easiest way to handle the
   different actions for each of your subparsers.  However, if it is necessary
   to check the name of the subparser that was invoked, the ``dest`` keyword
   argument to the :meth:`add_subparsers` call will work::

     &gt;&gt;&gt; parser = argparse.ArgumentParser()
     &gt;&gt;&gt; subparsers = parser.add_subparsers(dest='subparser_name')
     &gt;&gt;&gt; subparser1 = subparsers.add_parser('1')
     &gt;&gt;&gt; subparser1.add_argument('-x')
     &gt;&gt;&gt; subparser2 = subparsers.add_parser('2')
     &gt;&gt;&gt; subparser2.add_argument('y')
     &gt;&gt;&gt; parser.parse_args(['2', 'frobble'])
     Namespace(subparser_name='2', y='frobble')


</pre>
<a name="user-content-filetype-objects"></a>
<h3><a id="user-content-filetype-objects" class="anchor" aria-hidden="true" href="#filetype-objects"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>FileType objects</h3>
<p>The <a href="#id226">:class:`FileType`</a> factory creates objects that can be passed to the type
argument of <a href="#id228">:meth:`ArgumentParser.add_argument`</a>.  Arguments that have
<a href="#id230">:class:`FileType`</a> objects as their type will open command-line arguments as
files with the requested modes, buffer sizes, encodings and error handling
(see the <a href="#id232">:func:`open`</a> function for more details):</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser()
&gt;&gt;&gt; parser.add_argument('--raw', type=argparse.FileType('wb', 0))
&gt;&gt;&gt; parser.add_argument('out', type=argparse.FileType('w', encoding='UTF-8'))
&gt;&gt;&gt; parser.parse_args(['--raw', 'raw.dat', 'file.txt'])
Namespace(out=&lt;_io.TextIOWrapper name='file.txt' mode='w' encoding='UTF-8'&gt;, raw=&lt;_io.FileIO name='raw.dat' mode='wb'&gt;)
</pre>
<p>FileType objects understand the pseudo-argument <code>'-'</code> and automatically
convert this into <code>sys.stdin</code> for readable <a href="#id234">:class:`FileType`</a> objects and
<code>sys.stdout</code> for writable <a href="#id236">:class:`FileType`</a> objects:</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser()
&gt;&gt;&gt; parser.add_argument('infile', type=argparse.FileType('r'))
&gt;&gt;&gt; parser.parse_args(['-'])
Namespace(infile=&lt;_io.TextIOWrapper name='&lt;stdin&gt;' encoding='UTF-8'&gt;)
</pre>
<pre>.. versionadded:: 3.4
   The *encodings* and *errors* keyword arguments.
</pre>
<a name="user-content-argument-groups"></a>
<h3><a id="user-content-argument-groups" class="anchor" aria-hidden="true" href="#argument-groups"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Argument groups</h3>
<pre>.. method:: ArgumentParser.add_argument_group(title=None, description=None)

   By default, :class:`ArgumentParser` groups command-line arguments into
   "positional arguments" and "optional arguments" when displaying help
   messages. When there is a better conceptual grouping of arguments than this
   default one, appropriate groups can be created using the
   :meth:`add_argument_group` method::

     &gt;&gt;&gt; parser = argparse.ArgumentParser(prog='PROG', add_help=False)
     &gt;&gt;&gt; group = parser.add_argument_group('group')
     &gt;&gt;&gt; group.add_argument('--foo', help='foo help')
     &gt;&gt;&gt; group.add_argument('bar', help='bar help')
     &gt;&gt;&gt; parser.print_help()
     usage: PROG [--foo FOO] bar

     group:
       bar    bar help
       --foo FOO  foo help

   The :meth:`add_argument_group` method returns an argument group object which
   has an :meth:`~ArgumentParser.add_argument` method just like a regular
   :class:`ArgumentParser`.  When an argument is added to the group, the parser
   treats it just like a normal argument, but displays the argument in a
   separate group for help messages.  The :meth:`add_argument_group` method
   accepts *title* and *description* arguments which can be used to
   customize this display::

     &gt;&gt;&gt; parser = argparse.ArgumentParser(prog='PROG', add_help=False)
     &gt;&gt;&gt; group1 = parser.add_argument_group('group1', 'group1 description')
     &gt;&gt;&gt; group1.add_argument('foo', help='foo help')
     &gt;&gt;&gt; group2 = parser.add_argument_group('group2', 'group2 description')
     &gt;&gt;&gt; group2.add_argument('--bar', help='bar help')
     &gt;&gt;&gt; parser.print_help()
     usage: PROG [--bar BAR] foo

     group1:
       group1 description

       foo    foo help

     group2:
       group2 description

       --bar BAR  bar help

   Note that any arguments not in your user-defined groups will end up back
   in the usual "positional arguments" and "optional arguments" sections.


</pre>
<a name="user-content-mutual-exclusion"></a>
<h3><a id="user-content-mutual-exclusion" class="anchor" aria-hidden="true" href="#mutual-exclusion"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Mutual exclusion</h3>
<pre>.. method:: ArgumentParser.add_mutually_exclusive_group(required=False)

   Create a mutually exclusive group. :mod:`argparse` will make sure that only
   one of the arguments in the mutually exclusive group was present on the
   command line::

     &gt;&gt;&gt; parser = argparse.ArgumentParser(prog='PROG')
     &gt;&gt;&gt; group = parser.add_mutually_exclusive_group()
     &gt;&gt;&gt; group.add_argument('--foo', action='store_true')
     &gt;&gt;&gt; group.add_argument('--bar', action='store_false')
     &gt;&gt;&gt; parser.parse_args(['--foo'])
     Namespace(bar=True, foo=True)
     &gt;&gt;&gt; parser.parse_args(['--bar'])
     Namespace(bar=False, foo=False)
     &gt;&gt;&gt; parser.parse_args(['--foo', '--bar'])
     usage: PROG [-h] [--foo | --bar]
     PROG: error: argument --bar: not allowed with argument --foo

   The :meth:`add_mutually_exclusive_group` method also accepts a *required*
   argument, to indicate that at least one of the mutually exclusive arguments
   is required::

     &gt;&gt;&gt; parser = argparse.ArgumentParser(prog='PROG')
     &gt;&gt;&gt; group = parser.add_mutually_exclusive_group(required=True)
     &gt;&gt;&gt; group.add_argument('--foo', action='store_true')
     &gt;&gt;&gt; group.add_argument('--bar', action='store_false')
     &gt;&gt;&gt; parser.parse_args([])
     usage: PROG [-h] (--foo | --bar)
     PROG: error: one of the arguments --foo --bar is required

   Note that currently mutually exclusive argument groups do not support the
   *title* and *description* arguments of
   :meth:`~ArgumentParser.add_argument_group`.


</pre>
<a name="user-content-parser-defaults"></a>
<h3><a id="user-content-parser-defaults" class="anchor" aria-hidden="true" href="#parser-defaults"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Parser defaults</h3>
<pre>.. method:: ArgumentParser.set_defaults(**kwargs)

   Most of the time, the attributes of the object returned by :meth:`parse_args`
   will be fully determined by inspecting the command-line arguments and the argument
   actions.  :meth:`set_defaults` allows some additional
   attributes that are determined without any inspection of the command line to
   be added::

     &gt;&gt;&gt; parser = argparse.ArgumentParser()
     &gt;&gt;&gt; parser.add_argument('foo', type=int)
     &gt;&gt;&gt; parser.set_defaults(bar=42, baz='badger')
     &gt;&gt;&gt; parser.parse_args(['736'])
     Namespace(bar=42, baz='badger', foo=736)

   Note that parser-level defaults always override argument-level defaults::

     &gt;&gt;&gt; parser = argparse.ArgumentParser()
     &gt;&gt;&gt; parser.add_argument('--foo', default='bar')
     &gt;&gt;&gt; parser.set_defaults(foo='spam')
     &gt;&gt;&gt; parser.parse_args([])
     Namespace(foo='spam')

   Parser-level defaults can be particularly useful when working with multiple
   parsers.  See the :meth:`~ArgumentParser.add_subparsers` method for an
   example of this type.

</pre>
<pre>.. method:: ArgumentParser.get_default(dest)

   Get the default value for a namespace attribute, as set by either
   :meth:`~ArgumentParser.add_argument` or by
   :meth:`~ArgumentParser.set_defaults`::

     &gt;&gt;&gt; parser = argparse.ArgumentParser()
     &gt;&gt;&gt; parser.add_argument('--foo', default='badger')
     &gt;&gt;&gt; parser.get_default('foo')
     'badger'


</pre>
<a name="user-content-printing-help"></a>
<h3><a id="user-content-printing-help" class="anchor" aria-hidden="true" href="#printing-help"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Printing help</h3>
<p>In most typical applications, <a href="#id238">:meth:`~ArgumentParser.parse_args`</a> will take
care of formatting and printing any usage or error messages.  However, several
formatting methods are available:</p>
<pre>.. method:: ArgumentParser.print_usage(file=None)

   Print a brief description of how the :class:`ArgumentParser` should be
   invoked on the command line.  If *file* is ``None``, :data:`sys.stdout` is
   assumed.

</pre>
<pre>.. method:: ArgumentParser.print_help(file=None)

   Print a help message, including the program usage and information about the
   arguments registered with the :class:`ArgumentParser`.  If *file* is
   ``None``, :data:`sys.stdout` is assumed.

</pre>
<p>There are also variants of these methods that simply return a string instead of
printing it:</p>
<pre>.. method:: ArgumentParser.format_usage()

   Return a string containing a brief description of how the
   :class:`ArgumentParser` should be invoked on the command line.

</pre>
<pre>.. method:: ArgumentParser.format_help()

   Return a string containing a help message, including the program usage and
   information about the arguments registered with the :class:`ArgumentParser`.


</pre>
<a name="user-content-partial-parsing"></a>
<h3><a id="user-content-partial-parsing" class="anchor" aria-hidden="true" href="#partial-parsing"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Partial parsing</h3>
<pre>.. method:: ArgumentParser.parse_known_args(args=None, namespace=None)

</pre>
<p>Sometimes a script may only parse a few of the command-line arguments, passing
the remaining arguments on to another script or program. In these cases, the
<a href="#id240">:meth:`~ArgumentParser.parse_known_args`</a> method can be useful.  It works much like
<a href="#id242">:meth:`~ArgumentParser.parse_args`</a> except that it does not produce an error when
extra arguments are present.  Instead, it returns a two item tuple containing
the populated namespace and the list of remaining argument strings.</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser()
&gt;&gt;&gt; parser.add_argument('--foo', action='store_true')
&gt;&gt;&gt; parser.add_argument('bar')
&gt;&gt;&gt; parser.parse_known_args(['--foo', '--badger', 'BAR', 'spam'])
(Namespace(bar='BAR', foo=True), ['--badger', 'spam'])
</pre>
<div>
<p>Warning</p>
<p><a href="#id244">:ref:`Prefix matching &lt;prefix-matching&gt;`</a> rules apply to
<a href="#id246">:meth:`parse_known_args`</a>. The parser may consume an option even if it's just
a prefix of one of its known options, instead of leaving it in the remaining
arguments list.</p>
</div>
<a name="user-content-customizing-file-parsing"></a>
<h3><a id="user-content-customizing-file-parsing" class="anchor" aria-hidden="true" href="#customizing-file-parsing"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Customizing file parsing</h3>
<pre>.. method:: ArgumentParser.convert_arg_line_to_args(arg_line)

   Arguments that are read from a file (see the *fromfile_prefix_chars*
   keyword argument to the :class:`ArgumentParser` constructor) are read one
   argument per line. :meth:`convert_arg_line_to_args` can be overridden for
   fancier reading.

   This method takes a single argument *arg_line* which is a string read from
   the argument file.  It returns a list of arguments parsed from this string.
   The method is called once per line read from the argument file, in order.

   A useful override of this method is one that treats each space-separated word
   as an argument.  The following example demonstrates how to do this::

    class MyArgumentParser(argparse.ArgumentParser):
        def convert_arg_line_to_args(self, arg_line):
            return arg_line.split()


</pre>
<a name="user-content-exiting-methods"></a>
<h3><a id="user-content-exiting-methods" class="anchor" aria-hidden="true" href="#exiting-methods"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Exiting methods</h3>
<pre>.. method:: ArgumentParser.exit(status=0, message=None)

   This method terminates the program, exiting with the specified *status*
   and, if given, it prints a *message* before that.

</pre>
<pre>.. method:: ArgumentParser.error(message)

   This method prints a usage message including the *message* to the
   standard error and terminates the program with a status code of 2.


</pre>
<a name="user-content-intermixed-parsing"></a>
<h3><a id="user-content-intermixed-parsing" class="anchor" aria-hidden="true" href="#intermixed-parsing"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Intermixed parsing</h3>
<pre>.. method:: ArgumentParser.parse_intermixed_args(args=None, namespace=None)
</pre>
<pre>.. method:: ArgumentParser.parse_known_intermixed_args(args=None, namespace=None)

</pre>
<p>A number of Unix commands allow the user to intermix optional arguments with
positional arguments.  The <a href="#id248">:meth:`~ArgumentParser.parse_intermixed_args`</a>
and <a href="#id250">:meth:`~ArgumentParser.parse_known_intermixed_args`</a> methods
support this parsing style.</p>
<p>These parsers do not support all the argparse features, and will raise
exceptions if unsupported features are used.  In particular, subparsers,
<code>argparse.REMAINDER</code>, and mutually exclusive groups that include both
optionals and positionals are not supported.</p>
<p>The following example shows the difference between
<a href="#id252">:meth:`~ArgumentParser.parse_known_args`</a> and
<a href="#id254">:meth:`~ArgumentParser.parse_intermixed_args`</a>: the former returns <code>['2',
'3']</code> as unparsed arguments, while the latter collects all the positionals
into <code>rest</code>.</p>
<pre>&gt;&gt;&gt; parser = argparse.ArgumentParser()
&gt;&gt;&gt; parser.add_argument('--foo')
&gt;&gt;&gt; parser.add_argument('cmd')
&gt;&gt;&gt; parser.add_argument('rest', nargs='*', type=int)
&gt;&gt;&gt; parser.parse_known_args('doit 1 --foo bar 2 3'.split())
(Namespace(cmd='doit', foo='bar', rest=[1]), ['2', '3'])
&gt;&gt;&gt; parser.parse_intermixed_args('doit 1 --foo bar 2 3'.split())
Namespace(cmd='doit', foo='bar', rest=[1, 2, 3])
</pre>
<p><a href="#id256">:meth:`~ArgumentParser.parse_known_intermixed_args`</a> returns a two item tuple
containing the populated namespace and the list of remaining argument strings.
<a href="#id258">:meth:`~ArgumentParser.parse_intermixed_args`</a> raises an error if there are any
remaining unparsed argument strings.</p>
<pre>.. versionadded:: 3.7

</pre>
<a name="user-content-id260"></a>
<h2><a id="user-content-upgrading-optparse-code" class="anchor" aria-hidden="true" href="#upgrading-optparse-code"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Upgrading optparse code</h2>
<p>Originally, the <a href="#id261">:mod:`argparse`</a> module had attempted to maintain compatibility
with <a href="#id263">:mod:`optparse`</a>.  However, <a href="#id265">:mod:`optparse`</a> was difficult to extend
transparently, particularly with the changes required to support the new
<code>nargs=</code> specifiers and better usage messages.  When most everything in
<a href="#id267">:mod:`optparse`</a> had either been copy-pasted over or monkey-patched, it no
longer seemed practical to try to maintain the backwards compatibility.</p>
<p>The <a href="#id269">:mod:`argparse`</a> module improves on the standard library <a href="#id271">:mod:`optparse`</a>
module in a number of ways including:</p>
<ul>
<li>Handling positional arguments.</li>
<li>Supporting sub-commands.</li>
<li>Allowing alternative option prefixes like <code>+</code> and <code>/</code>.</li>
<li>Handling zero-or-more and one-or-more style arguments.</li>
<li>Producing more informative usage messages.</li>
<li>Providing a much simpler interface for custom <code>type</code> and <code>action</code>.</li>
</ul>
<p>A partial upgrade path from <a href="#id273">:mod:`optparse`</a> to <a href="#id275">:mod:`argparse`</a>:</p>
<ul>
<li>Replace all <a href="#id277">:meth:`optparse.OptionParser.add_option`</a> calls with
<a href="#id279">:meth:`ArgumentParser.add_argument`</a> calls.</li>
<li>Replace <code>(options, args) = parser.parse_args()</code> with <code>args =
parser.parse_args()</code> and add additional <a href="#id281">:meth:`ArgumentParser.add_argument`</a>
calls for the positional arguments. Keep in mind that what was previously
called <code>options</code>, now in the <a href="#id283">:mod:`argparse`</a> context is called <code>args</code>.</li>
<li>Replace <a href="#id285">:meth:`optparse.OptionParser.disable_interspersed_args`</a>
by using <a href="#id287">:meth:`~ArgumentParser.parse_intermixed_args`</a> instead of
<a href="#id289">:meth:`~ArgumentParser.parse_args`</a>.</li>
<li>Replace callback actions and the <code>callback_*</code> keyword arguments with
<code>type</code> or <code>action</code> arguments.</li>
<li>Replace string names for <code>type</code> keyword arguments with the corresponding
type objects (e.g. int, float, complex, etc).</li>
<li>Replace <a href="#id291">:class:`optparse.Values`</a> with <a href="#id293">:class:`Namespace`</a> and
<a href="#id295">:exc:`optparse.OptionError`</a> and <a href="#id297">:exc:`optparse.OptionValueError`</a> with
<a href="#id299">:exc:`ArgumentError`</a>.</li>
<li>Replace strings with implicit arguments such as <code>%default</code> or <code>%prog</code> with
the standard Python syntax to use dictionaries to format strings, that is,
<code>%(default)s</code> and <code>%(prog)s</code>.</li>
<li>Replace the OptionParser constructor <code>version</code> argument with a call to
<code>parser.add_argument('--version', action='version', version='&lt;the version&gt;')</code>.</li>
</ul>

</article>
  </div>

  </div>

  <button type="button" data-facebox="#jump-to-line" data-facebox-class="linejump" data-hotkey="l" class="d-none">Jump to Line</button>
  <div id="jump-to-line" style="display:none">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-jump-to-line-form" action="" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
      <input class="form-control linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" aria-label="Jump to line" autofocus>
      <button type="submit" class="btn">Go</button>
</form>  </div>


  </div>
  <div class="modal-backdrop js-touch-events"></div>
</div>

    </div>
  </div>

  </div>

      
<div class="footer container-lg px-3" role="contentinfo">
  <div class="position-relative d-flex flex-justify-between pt-6 pb-2 mt-6 f6 text-gray border-top border-gray-light ">
    <ul class="list-style-none d-flex flex-wrap ">
      <li class="mr-3">&copy; 2018 <span title="0.36537s from unicorn-4201435213-nfts6">GitHub</span>, Inc.</li>
        <li class="mr-3"><a data-ga-click="Footer, go to terms, text:terms" href="https://github.com/site/terms">Terms</a></li>
        <li class="mr-3"><a data-ga-click="Footer, go to privacy, text:privacy" href="https://github.com/site/privacy">Privacy</a></li>
        <li class="mr-3"><a href="https://help.github.com/articles/github-security/" data-ga-click="Footer, go to security, text:security">Security</a></li>
        <li class="mr-3"><a href="https://status.github.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
        <li><a data-ga-click="Footer, go to help, text:help" href="https://help.github.com">Help</a></li>
    </ul>

    <a aria-label="Homepage" title="GitHub" class="footer-octicon" href="https://github.com">
      <svg height="24" class="octicon octicon-mark-github" viewBox="0 0 16 16" version="1.1" width="24" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
</a>
   <ul class="list-style-none d-flex flex-wrap ">
        <li class="mr-3"><a data-ga-click="Footer, go to contact, text:contact" href="https://github.com/contact">Contact GitHub</a></li>
      <li class="mr-3"><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li class="mr-3"><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
      <li class="mr-3"><a href="https://shop.github.com" data-ga-click="Footer, go to shop, text:shop">Shop</a></li>
        <li class="mr-3"><a href="https://blog.github.com" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a data-ga-click="Footer, go to about, text:about" href="https://github.com/about">About</a></li>

    </ul>
  </div>
  <div class="d-flex flex-justify-center pb-6">
    <span class="f6 text-gray-light"></span>
  </div>
</div>



  <div id="ajax-error-message" class="ajax-error-message flash flash-error">
    <svg class="octicon octicon-alert" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.893 1.5c-.183-.31-.52-.5-.887-.5s-.703.19-.886.5L.138 13.499a.98.98 0 0 0 0 1.001c.193.31.53.501.886.501h13.964c.367 0 .704-.19.877-.5a1.03 1.03 0 0 0 .01-1.002L8.893 1.5zm.133 11.497H6.987v-2.003h2.039v2.003zm0-3.004H6.987V5.987h2.039v4.006z"/></svg>
    <button type="button" class="flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
    </button>
    You can’t perform that action at this time.
  </div>


    <script crossorigin="anonymous" integrity="sha512-wIuAKDhvxe9wCaNR1tzCk3rtl+wXEWC28rmRpzmx0h98VEeWC6Y3xCWV1xAW6NP6eQQX+x8ZGhW6Sdut+mLRuw==" type="application/javascript" src="https://assets-cdn.github.com/assets/compat-a48960bafc17c30572990bbab3664e9c.js"></script>
    <script crossorigin="anonymous" integrity="sha512-LB1tzJRQ5uPC9BeR2Mb4TOIBPBxMXSM2p2+WgU7lLEdqAe7TptfwpDfDqfAnWlC2aw7FoJcKQxqDyjulVPpIbw==" type="application/javascript" src="https://assets-cdn.github.com/assets/frameworks-ad697dde9ac7f691157024c54b447026.js"></script>
    
    <script crossorigin="anonymous" async="async" integrity="sha512-Tqd1j3zgJYL8NSjEw4UYqRS4kQ09vPAu4KWouT3+gnnt5Mupx/Ps2ZM/CdF6oa1L0dw+vxRHaAkgkpcahIX40g==" type="application/javascript" src="https://assets-cdn.github.com/assets/github-e10f06304c6b9fd853406284acc0fe0a.js"></script>
    
    
    
  <div class="js-stale-session-flash stale-session-flash flash flash-warn flash-banner d-none">
    <svg class="octicon octicon-alert" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.893 1.5c-.183-.31-.52-.5-.887-.5s-.703.19-.886.5L.138 13.499a.98.98 0 0 0 0 1.001c.193.31.53.501.886.501h13.964c.367 0 .704-.19.877-.5a1.03 1.03 0 0 0 .01-1.002L8.893 1.5zm.133 11.497H6.987v-2.003h2.039v2.003zm0-3.004H6.987V5.987h2.039v4.006z"/></svg>
    <span class="signed-in-tab-flash">You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
    <span class="signed-out-tab-flash">You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
  </div>
  <div class="facebox" id="facebox" style="display:none;">
  <div class="facebox-popup">
    <div class="facebox-content" role="dialog" aria-labelledby="facebox-header" aria-describedby="facebox-description">
    </div>
    <button type="button" class="facebox-close js-facebox-close" aria-label="Close modal">
      <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
    </button>
  </div>
</div>

  <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none;" tabindex="0">
  <div class="Popover-message Popover-message--bottom-left Popover-message--large Box box-shadow-large" style="width:360px;">
  </div>
</div>

<div id="hovercard-aria-description" class="sr-only">
  Press h to open a hovercard with more details.
</div>


  </body>
</html>

