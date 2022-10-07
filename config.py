from datetime import date

today = date.today()
schedule_remote_csv_path = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRHQ4v3xFDgclHRL13fj8TJ_ohJxlewvsXWOrdPHMB8qbx8vSdLyHmZB4hkYrj88K10zufZCrZ_jFmX/pub?output=csv"
schedule_local_csv_name = "schedule.csv"
schedule_local_markdown_name = "README.md"

markdown_strings_speaker_info = [
    f"""![code-along-logo](/assets/img/code-along-with-alex-logo.svg)\n""",
    f"""\n""",
    f"""## Who\n""",
    f"""Sessions are guided by [Alex Pakalniskis](https://barracuda.io/paka), an engineer working in web2 and web3\n""",
    f"""\n""",
    f"""## Where\n""",
    f"""[Graph AdvocatesDAO Discord](https://t.co/xYb6Fgb98n)\n""",
    f"""* 🎤-public-voice-chat\n""",
    f"""\n""",
]

markdown_strings_multisession_repos = [
    f"""## Repositories for multi-session projects\n""",
    f"""* [Rust by Example](https://github.com/alex-pakalniskis/CodeAlong-RustByExample)\n""",
    f"""* [Containerized Python Application](https://github.com/alex-pakalniskis/CodeAlong-ContainerizedPythonApplication)\n"""
    f"""\n"""
]

markdown_strings_request_content = [
    f"""## Request content\n""",
    f"""Please [open a new issue](https://github.com/alex-pakalniskis/CodeAlongSchedule/issues/new) to request specific code along content\n""",
    f"""\n"""
]
