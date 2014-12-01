from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from Products.CMFCore.utils import getToolByName

class SiteTitle(ViewletBase):
    render = ViewPageTemplateFile('sitetitle.pt')

    def update(self):
        portal_url = getToolByName(self.context, "portal_url")
        portal = portal_url.getPortalObject()
        
        self.title = portal.title

class UWOshTopLinksViewlet(ViewletBase):
    render = ViewPageTemplateFile('uwosh_top_links_viewlet.pt')
    
    def update(self):
        open_in_new_window = True
        if open_in_new_window:
            target = 'target="_blank"'
        else:  
            target = ''        
        prefix = '<dl class="actionMenu deactivated" id="uwoshtoplinkswrapper"> <dt id="uwoshtoplinks">'
        postfix = '</dt></dl>'
        middle = ''
        p_actions = getToolByName(self, 'portal_actions', None)
        if p_actions:
            top_links = getattr(p_actions, 'uwosh_toplinks', None)
            if top_links:
                for linkId in top_links:
                    a = top_links[linkId]
                    url = a.getProperty('url_expr').replace('string:','')
                    title = a.getProperty('title')
                    visible = a.getProperty('visible')
                    if visible:
                        middle += '<a id="uwoshtoplink-%s" href="%s" %s>%s</a>' % (linkId, url, target, title)
        self.computed_value = prefix + middle + postfix
