DOCUMENTS = [
    {"tenant_id": "alpha", "text": "alpha policy"},
    {"tenant_id": "beta", "text": "beta policy"},
]


def search(user_tenant, query):
    return [
        document
        for document in DOCUMENTS
        if document["tenant_id"] == user_tenant
        and query.lower() in document["text"].lower()
    ]


def main():
    tenant = input("Authenticated tenant_id: ").strip() or "alpha"
    query = input("Query: ").strip() or "policy"
    print("filtered_results:", search(tenant, query))
    print(
        "isolation_check:",
        all(item["tenant_id"] == tenant for item in search(tenant, query)),
    )


if __name__ == "__main__":
    main()
