Feature: Team Fortress 2 status

  Scenario: User get his Team Fortress 2 Status
    Given gutomaia as user
     When he asks for the tf2 status
     Then the gameName is Team Fortress 2