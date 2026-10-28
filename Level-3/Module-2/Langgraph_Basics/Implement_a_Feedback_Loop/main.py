def support(issue, rating):
    state = {"issue": issue, "satisfaction_rating": rating}
    if rating < 3:
        state["next"] = "understand_issue"
    else:
        state["next"] = "END"
    return state


def main():
    rating = int(input("Rating 1-5 [4]: ") or 4)
    print(support("customer complaint", rating))


if __name__ == "__main__":
    main()
