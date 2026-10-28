def approvals(sender, draft):
    vip = sender.lower().endswith("@enterprise-client.com")
    decisions = ["support"]
    if vip:
        decisions.append("manager")
    return {"vip_approval": vip, "required": decisions, "draft": draft, "approved": True}


def main():
    print(approvals(input("Sender: ") or "user@example.com", "Draft response"))


if __name__ == "__main__":
    main()
