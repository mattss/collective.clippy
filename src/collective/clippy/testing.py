from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile

from zope.configuration import xmlconfig

class CollectiveClippy(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import collective.clippy
        xmlconfig.file('configure.zcml',
                       collective.clippy,
                       context=configurationContext)


    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.clippy:default')

COLLECTIVE_CLIPPY_FIXTURE = CollectiveClippy()
COLLECTIVE_CLIPPY_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(COLLECTIVE_CLIPPY_FIXTURE, ),
                       name="CollectiveClippy:Integration")