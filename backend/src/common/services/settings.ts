import { SettingsEnum } from "../../controllers/settingsController/models/ISettings"
import Setting, { ISetting, ISettingDocument } from "../../models/setting.model"

export default class SettingsService {
  public static getDefaultSettingsIds(settings: ISettingDocument[]) {
    return settings.map(({ _id }) => _id)
  }

  private defaultSettings: ISetting[] = [
    {
      key: SettingsEnum.BotResponseChannelId,
      value: String.empty
    },
    {
      key: SettingsEnum.MonthlyKudosAmount,
      value: '100'
    },
    {
      key: SettingsEnum.GiftRequestsReceiver,
      value: String.empty
    }
  ]

  public async createDefaultSettings() {
    return await Setting.insertMany(this.defaultSettings)
  }

  public updateSetting(id: string, value: string) {
    return Setting.findByIdAndUpdate(id, { value })
  }
}
