import asyncio
from nextgraphpy import wallet_open_with_mnemonic_words, doc_sparql_update, disconnect_and_close

async def main():
    wallet_session = await wallet_open_with_mnemonic_words(
        "/home/nn/Downloads/wallet-bCHhOmlelVtZ60jjGu7m-YtzF4TfD5WyErAMnEDOn-kA.ngw", 
        ["mutual", "wife", "section", "actual", "spend", "illness", "save", "delay", "kiss", "crash", "baby", "degree" ],
        [2, 3, 2, 3])
    wallet_name = wallet_session[0]
    session_info = wallet_session[1]
    print(wallet_name)
    print(session_info)
    commits = await doc_sparql_update(session_info["session_id"], 
        "INSERT DATA { <did:ng:_> <example:predicate> \"An example value22\". }")
    print(commits)
    await disconnect_and_close(session_info["user"], wallet_name)

asyncio.run(main())