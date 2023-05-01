import os
import requests
from dotenv import load_dotenv
from github import Github
from github import RateLimitExceededException
from datetime import datetime, timedelta
import pandas as pd

load_dotenv()

access_token = os.environ.get("ACCESS_TOKEN")

g = Github(access_token)

repositories = [
    "ethereum/go-ethereum",
    "solana-labs/solana",
    "maticnetwork/bor",
    "paritytech/polkadot",
    "cosmos/cosmos-sdk",
    "algorand/go-algorand",
    "ava-labs/avalanchego",
    "input-output-hk/cardano-node",
    "EOSIO/eos",
    "vechain/thor",
    "ethereum-optimism/optimism",
    "OffchainLabs/arbitrum"
]

data = {'Repository': [], 'Number of contributors': [], 'Number of releases in the past year': [],
        'Active contributors': []}

for repo_name in repositories:
    try:
        repo = g.get_repo(repo_name)

        contributors = repo.get_contributors()
        contributors_count = contributors.totalCount
        print(repo_name, contributors_count)

        headers = {'Authorization': f'token {access_token}'}

        releases = repo.get_releases()
        one_year_ago = datetime.now() - timedelta(days=365)

        yearly_releases = 0

        for release in releases:
            release_url = release.url
            response = requests.get(release_url, headers=headers)

            if response.status_code == 200:
                release_data = response.json()
                release_date = datetime.strptime(release_data['published_at'], '%Y-%m-%dT%H:%M:%SZ')

                if release_date > one_year_ago:
                    yearly_releases += 1

        # active_contributors = []
        #
        # for contributor in contributors:
        #     commits = repo.get_commits(author=contributor)
        #     recent_commits = [commit for commit in commits if commit.commit.author.date > one_year_ago]
        #     if len(recent_commits) > 50:
        #         active_contributors.append(contributor.login)

        data['Repository'].append(repo_name)
        data['Number of contributors'].append(contributors_count)
        data['Number of releases in the past year'].append(yearly_releases)
        # data['Active contributors'].append(', '.join(active_contributors))

    except RateLimitExceededException:
        print("Rate limit exceeded. Please wait for the rate limit to reset.")
        break

df = pd.DataFrame(data, columns=['Repository', 'Number of contributors', 'Number of releases in the past year'])
# 'Active contributors']

print(df)
