
from click import command
from click import option
from click import version_option
from click import ClickException

from versionoverlord import __version__

from versionoverlord.Common import EPILOG
from versionoverlord.Common import RepositorySlug
from versionoverlord.Common import setUpLogging

from versionoverlord.githubadapter.GitHubAdapter import GitHubAdapter
from versionoverlord.githubadapter.GitHubAdapterTypes import ReleaseTitle
from versionoverlord.githubadapter.GitHubAdapterError import GitHubAdapterError


@command(epilog=EPILOG)
@version_option(version=f'{__version__}', message='%(prog)s version %(version)s')
@option('--slug',          '-s', required=True,  help='GitHub slug')
@option('--release-title', '-r', required=True,  help='The title of the release to publish')
def publishRelease(slug: RepositorySlug, release_title: ReleaseTitle):
    """
    \b
    The short name is 'pub' instead of 'pr' so as not to conflict with the *nix command
    for print files

    \b
    It uses the following environment variables:

    \b
        GH_TOKEN      – A personal GitHub access token necessary to read repository release information
        PROJECTS_BASE – The local directory where the python projects are based
        PROJECT       – The name of the project;  It should be a directory name
    """
    try:
        gitHubAdapter: GitHubAdapter = GitHubAdapter()

        gitHubAdapter.publishRelease(repositorySlug=slug, releaseTitle=release_title)

    except GitHubAdapterError as e:
        raise ClickException(message=e.message)


if __name__ == "__main__":
    setUpLogging()

    # publishRelease(['--version'])
    # publishRelease(['--help'])
    publishRelease(['--slug', 'hasii2011/TestRepository', '--release-title', 'Fake Release Name'])
