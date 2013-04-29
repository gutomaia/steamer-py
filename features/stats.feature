Feature: Testing the stats

  Scenario: User get his Team Fortress 2 Status
    Given gutomaia as user
     When he asks for the tf2 status
     Then the gameName is Team Fortress 2
     And the gameFriendlyName is TF2

  Scenario: User get his Left 4 Dead 2 Status
    Given gutomaia as user
     When he asks for the l4d2 status
     Then the gameName is Left 4 Dead 2
     And the gameFriendlyName is L4D2

  Scenario: User get his Portal 2 Status
    Given gutomaia as user
     When he asks for the portal2 status
     Then the gameName is Portal 2
     And the gameFriendlyName is Portal2