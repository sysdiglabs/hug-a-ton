import { MessageAttachment } from "@slack/client"
import { IMessageConsumer, ISlackCommandInfo } from "../../controllers/definitions/slackController"
import { SlackResponseType } from "../factories/definitions/slackCommandHandlerFactory"
import LoggerService from "../services/logger"
import SlackClientService from "../services/slackClient"
import TranslationsService from "../services/translationsService"
import UserService from "../services/user"

abstract class BaseSlackCommandHandler {
  get commandText() {
    const { text } = this.commandInfo

    return text
  }

  get senderId() {
    const { user_id } = this.commandInfo

    return user_id
  }

  get teamId() {
    const { team_id } = this.commandInfo

    return team_id
  }

  get messageConsumer() {
    const { team_id, channel_id, user_id } = this.commandInfo
    const messageConsumer: IMessageConsumer = {
      channel: channel_id,
      teamId: team_id,
      user: user_id
    }

    return messageConsumer
  }

  protected translationsService = new TranslationsService()
  protected slackClientService = new SlackClientService()
  protected userService = new UserService()
  protected logger = new LoggerService()

  constructor(protected commandInfo: ISlackCommandInfo) { }

  public sendMessage(
    text: string,
    consumer: IMessageConsumer,
    type?: SlackResponseType,
    attachments?: MessageAttachment[]
  ): void {
    this.slackClientService.sendMessage(text, consumer, type, attachments)
  }

  public async handleCommand(): Promise<void> {
    try {
      await this.validate()
      await this.onHandleCommand()
    } catch ({ message }) {
      this.sendMessage(
        message,
        this.messageConsumer,
        SlackResponseType.hidden
      )
    }
  }

  public abstract onHandleCommand(): void

  public getCustomMessageConsumer(
    teamId: string,
    channel: string,
    user?: string
  ): IMessageConsumer {
    return { teamId, channel, user }
  }

  protected async validate(): Promise<void> {
    return
  }
}

export default BaseSlackCommandHandler
