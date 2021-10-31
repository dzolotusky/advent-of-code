package com.spotify;

public class Year2021Day23Activity2 {
    public static void main(String[] args) {
    Year2021Day23Activity2 activityObject = new Year2021Day23Activity2();
    activityObject.run();
  }

  private class cup {
    cup next;
    int value;
    public cup()
    {

    }

    public cup(int newValue, cup nextCard) {
      value = newValue;
      next = nextCard;
    }

  }

  // test input is new int[]{3,8,9,1,2,5,4,6,7};
  // real input is new int[]{9,4,2,3,8,7,6,1,5};
  int[] initialVal = new int[]{9,4,2,3,8,7,6,1,5};
  private int num_moves = 10000000; // test is 100;  //real is 10000000
  private cup allCups;
  private cup[] cupArray = new cup[1000001];

  public void setup() {
    cup nextCup = new cup();
    allCups = nextCup;
    for (int i = 0; i < 1000000; i++) {
      if (i < initialVal.length) {
        cupArray[initialVal[i]] = nextCup;
        nextCup.value = initialVal[i];
      }
      else {
        cupArray[i + 1] = nextCup;
        nextCup.value = i + 1;
      }

      if (i + 1 < 1000000) {
        nextCup.next = new cup();
        nextCup = nextCup.next;
      } else {
        nextCup.next = allCups;
      }
    }

    // fill out until 1000000 for real version
  }

  public void run() {
    setup();
    cup currentCup = allCups;;
    cup removed;
    cup destinationCup;

    for (int move_num = 0; move_num < num_moves; move_num++) {
      removed = currentCup.next;
      currentCup.next = removed.next.next.next;

      int destinationCupValue = currentCup.value - 1;
      if (destinationCupValue < 1) {
        destinationCupValue = cupArray.length - 1;
      }

      while (destinationCupValue == removed.value || destinationCupValue == removed.next.value
                                                     | destinationCupValue
                                                       == removed.next.next.value) {
        destinationCupValue -= 1;
        if (destinationCupValue < 1) {
          destinationCupValue = cupArray.length - 1;
        }
      }

      destinationCup = cupArray[destinationCupValue];
      removed.next.next.next = destinationCup.next;
      destinationCup.next = removed;
      currentCup = currentCup.next;
    }

    cup cupOne = cupArray[1];
    System.out.print("part 2 = ");
    long part2 = ((long)cupOne.next.value) * cupOne.next.next.value;
    System.out.println(part2);
  }
}
